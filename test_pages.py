import urllib.request
pages = ['', 'about/', 'services/', 'results/', 'contact/']
for p in pages:
    try:
        status = urllib.request.urlopen(f'http://127.0.0.1:8000/{p}').status
        print(f'{p or "home"}: {status}')
    except Exception as e:
        print(f'{p or "home"}: ERROR - {e}')
