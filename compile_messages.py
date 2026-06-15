"""Compile .po files to .mo files using Python's msgfmt module."""
import os
import sys

# Python ships with Tools/i18n/msgfmt.py or we can use the msgfmt module
try:
    from Tools.i18n import msgfmt as _msgfmt
except ImportError:
    pass

import struct
import codecs

def unescape(val):
    return codecs.escape_decode(val.encode('utf-8'))[0].decode('utf-8')

def compile_po(po_path, mo_path):
    """Minimal .po to .mo compiler."""
    messages = {}
    msgid = None
    msgstr_lines = []
    in_msgstr = False
    
    with open(po_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            if line.startswith('msgid '):
                if msgid is not None and in_msgstr:
                    clean_id = unescape(msgid)
                    clean_str = unescape(''.join(msgstr_lines))
                    messages[clean_id] = clean_str
                msgid_text = line[6:].strip('"')
                msgid = msgid_text
                msgstr_lines = []
                in_msgstr = False
            elif line.startswith('msgstr '):
                msgstr_text = line[7:].strip('"')
                msgstr_lines = [msgstr_text]
                in_msgstr = True
            elif line.startswith('"') and in_msgstr:
                msgstr_lines.append(line.strip('"'))
            elif line.startswith('"') and not in_msgstr:
                msgid = (msgid or '') + line.strip('"')
        
        if msgid is not None and in_msgstr:
            clean_id = unescape(msgid)
            clean_str = unescape(''.join(msgstr_lines))
            messages[clean_id] = clean_str
    
    # We MUST keep the empty msgid (header) because it contains the charset info!
    # Remove entries with empty translations (but keep the empty msgid header)
    messages = {k: v for k, v in messages.items() if v or k == ''}
    
    # Build .mo file
    keys = sorted(messages.keys())
    offsets = []
    ids = b''
    strs = b''
    
    for key in keys:
        id_bytes = key.encode('utf-8')
        str_bytes = messages[key].encode('utf-8')
        offsets.append((len(ids), len(id_bytes), len(strs), len(str_bytes)))
        ids += id_bytes + b'\x00'
        strs += str_bytes + b'\x00'
    
    n = len(keys)
    keystart = 28
    valuestart = keystart + n * 8
    koffsets = []
    voffsets = []
    
    ids_start = valuestart + n * 8
    strs_start = ids_start + len(ids)
    
    for o in offsets:
        koffsets.append((o[1], ids_start + o[0]))
        voffsets.append((o[3], strs_start + o[2]))
    
    output = struct.pack('Iiiiiii',
        0x950412de,  # Magic
        0,           # Version
        n,           # Number of strings
        keystart,    # Offset of key table
        valuestart,  # Offset of value table
        0,           # Size of hashing table
        0,           # Offset of hashing table
    )
    
    for length, offset in koffsets:
        output += struct.pack('ii', length, offset)
    for length, offset in voffsets:
        output += struct.pack('ii', length, offset)
    
    output += ids + strs
    
    os.makedirs(os.path.dirname(mo_path), exist_ok=True)
    with open(mo_path, 'wb') as f:
        f.write(output)
    
    return n

# Find and compile all .po files
base = os.path.dirname(os.path.abspath(__file__))
locale_dir = os.path.join(base, 'locale')
total = 0

for lang in os.listdir(locale_dir):
    po_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.mo')
    if os.path.exists(po_path):
        n = compile_po(po_path, mo_path)
        print(f'{lang}: compiled {n} messages -> {mo_path}')
        total += n

print(f'\nTotal: {total} messages compiled')
