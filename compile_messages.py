"""Compile all .po files to .mo files using pure Python — with proper headers and escaping."""
import struct
import os
import re
import codecs

def compile_po(po_path):
    mo_path = po_path.replace('.po', '.mo')
    messages = {}
    
    with open(po_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    entry = {'msgid': None, 'msgstr': None}
    current_key = None # 'msgid' or 'msgstr'
    
    def unescape(s):
        if s is None:
            return ""
        # codecs.escape_decode parses escape sequences like \n, \t, \", \\ etc.
        try:
            return codecs.escape_decode(s.encode('utf-8'))[0].decode('utf-8')
        except Exception:
            return s

    def add_current_entry():
        if entry['msgid'] is not None and entry['msgstr'] is not None:
            msgid = unescape(entry['msgid'])
            msgstr = unescape(entry['msgstr'])
            messages[msgid] = msgstr
            entry['msgid'] = None
            entry['msgstr'] = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        if line.startswith('msgid '):
            add_current_entry()
            m = re.match(r'^msgid\s+"(.*)"$', line)
            if m:
                entry['msgid'] = m.group(1)
                current_key = 'msgid'
        elif line.startswith('msgstr '):
            m = re.match(r'^msgstr\s+"(.*)"$', line)
            if m:
                entry['msgstr'] = m.group(1)
                current_key = 'msgstr'
        elif line.startswith('"') and line.endswith('"'):
            m = re.match(r'^"(.*)"$', line)
            if m and current_key:
                entry[current_key] += m.group(1)
                
    add_current_entry()
    
    # Ensure there is a charset header
    if '' not in messages or 'charset=' not in messages['']:
        messages[''] = (
            'Content-Type: text/plain; charset=UTF-8\n'
            'Content-Transfer-Encoding: 8bit\n'
        )
    else:
        # Force charset to UTF-8 just in case
        header = messages['']
        if 'charset=ascii' in header.lower():
            header = re.sub(r'charset=\S+', 'charset=UTF-8', header, flags=re.IGNORECASE)
            messages[''] = header

    # Build MO file
    keys = sorted(messages.keys())
    n = len(keys)
    
    keystart = 28
    valuestart = keystart + n * 8
    data_start = valuestart + n * 8
    
    ids_data = b''
    strs_data = b''
    key_offsets = []
    val_offsets = []
    
    for key in keys:
        id_bytes = key.encode('utf-8')
        str_bytes = messages[key].encode('utf-8')
        key_offsets.append((len(id_bytes), len(ids_data)))
        val_offsets.append((len(str_bytes), len(strs_data)))
        ids_data += id_bytes + b'\0'
        strs_data += str_bytes + b'\0'
    
    ids_offset = data_start
    strs_offset = data_start + len(ids_data)
    
    output = struct.pack(
        'Iiiiiii',
        0x950412de, 0, n, keystart, valuestart, 0, 0
    )
    
    for length, offset in key_offsets:
        output += struct.pack('ii', length, ids_offset + offset)
    
    for length, offset in val_offsets:
        output += struct.pack('ii', length, strs_offset + offset)
    
    output += ids_data + strs_data
    
    with open(mo_path, 'wb') as f:
        f.write(output)
    
    print(f'  Compiled: {mo_path} ({n} entries)')

languages = ['ar', 'de', 'en', 'es', 'it', 'nl']
for lang in languages:
    po_file = os.path.join('locale', lang, 'LC_MESSAGES', 'django.po')
    if os.path.exists(po_file):
        compile_po(po_file)
    else:
        print(f'  Missing: {po_file}')

print('All translations compiled!')
