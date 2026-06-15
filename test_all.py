"""Verify translations, URLs, logo, and site name."""
import urllib.request

checks = []

# Test translated site names
for lang, expected_name in [('en', 'International Laboratory'), ('es', 'Laboratorio Internacional'), ('de', 'Internationales Labor'), ('nl', 'Internationaal Laboratorium')]:
    r = urllib.request.urlopen(f'http://127.0.0.1:8000/{lang}/').read().decode()
    ok = expected_name in r
    checks.append((f'{lang} site name: {expected_name}', ok))

# Test logo image
r = urllib.request.urlopen('http://127.0.0.1:8000/fr/').read().decode()
checks.append(('Logo image tag', 'logo.png' in r))
checks.append(('No flask icon in nav', 'fa-flask text-white text-lg' not in r))

# Test translated URLs in nav links
for lang, expected in [('es', 'servicios'), ('de', 'leistungen'), ('nl', 'diensten')]:
    r = urllib.request.urlopen(f'http://127.0.0.1:8000/{lang}/').read().decode()
    checks.append((f'{lang} URL has "{expected}"', expected in r))

# Test translated URLs work (200 OK)
url_tests = [
    ('http://127.0.0.1:8000/es/servicios/', 'ES services URL'),
    ('http://127.0.0.1:8000/de/leistungen/', 'DE services URL'),
    ('http://127.0.0.1:8000/nl/diensten/', 'NL services URL'),
    ('http://127.0.0.1:8000/en/services/', 'EN services URL'),
    ('http://127.0.0.1:8000/es/contacto/', 'ES contact URL'),
    ('http://127.0.0.1:8000/de/kontakt/', 'DE contact URL'),
]
for url, label in url_tests:
    try:
        code = urllib.request.urlopen(url).getcode()
        checks.append((f'{label} ({url})', code == 200))
    except Exception as e:
        checks.append((f'{label} ({url})', False))
        print(f'  ERROR: {e}')

# Test slogan translation
for lang, expected in [('en', 'Medical Laboratory'), ('es', 'Laboratorio de'), ('de', 'Medizinisches Labor'), ('nl', 'Medisch Laboratorium')]:
    r = urllib.request.urlopen(f'http://127.0.0.1:8000/{lang}/').read().decode()
    checks.append((f'{lang} slogan: {expected}', expected in r))

passed = sum(1 for _, ok in checks if ok)
failed = sum(1 for _, ok in checks if not ok)
for label, ok in checks:
    status = 'PASS' if ok else 'FAIL'
    if not ok:
        print(f'  {status}: {label}')

print(f'\nResults: {passed} passed, {failed} failed out of {len(checks)} checks')
