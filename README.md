# Capa de Comunicacion de app con robot

interface=wlan0
driver=nl80211
ssid=TU_NOMBRE_DE_RED
hw_mode=g
channel=7
wpa=2
wpa_passphrase=TU_CONTRASEÑA
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP


interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h

Job for hostapd.service failed because the control process exited with error code.
See "systemctl status hostapd.service" and "journalctl -xe" for details.

● hostapd.service - Access point and authentication server for Wi-Fi and Ethernet
     Loaded: loaded (/lib/systemd/system/hostapd.service; enabled; vendor preset: enabled)
     Active: activating (auto-restart) (Result: exit-code) since Sat 2023-06-10 18:26:26 BST; 696ms ago
       Docs: man:hostapd(8)
    Process: 2046 ExecStart=/usr/sbin/hostapd -B -P /run/hostapd.pid -B $DAEMON_OPTS ${DAEMON_CONF} (code=exited, status=1/FAILURE)
        CPU: 19ms

Jun 10 18:26:26 raspberrypi systemd[1]: Failed to start Access point and authentication server for Wi-Fi and Ethernet.





Traceback (most recent call last):
  File "/home/eva/.local/bin/celery", line 8, in <module>
    sys.exit(main())
  File "/home/eva/.local/lib/python3.9/site-packages/celery/__main__.py", line 15, in main
    sys.exit(_main())
  File "/home/eva/.local/lib/python3.9/site-packages/celery/bin/celery.py", line 235, in main
    return celery(auto_envvar_prefix="CELERY")
  File "/home/eva/.local/lib/python3.9/site-packages/click/core.py", line 1130, in __call__
    return self.main(*args, **kwargs)
  File "/home/eva/.local/lib/python3.9/site-packages/click/core.py", line 1055, in main
    rv = self.invoke(ctx)
  File "/home/eva/.local/lib/python3.9/site-packages/click/core.py", line 1657, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/home/eva/.local/lib/python3.9/site-packages/click/core.py", line 1404, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/eva/.local/lib/python3.9/site-packages/click/core.py", line 760, in invoke
    return __callback(*args, **kwargs)
  File "/home/eva/.local/lib/python3.9/site-packages/click/decorators.py", line 26, in new_func
    return f(get_current_context(), *args, **kwargs)
  File "/home/eva/.local/lib/python3.9/site-packages/celery/bin/base.py", line 134, in caller
    return f(ctx, *args, **kwargs)
  File "/home/eva/.local/lib/python3.9/site-packages/celery/bin/worker.py", line 348, in worker
    worker = app.Worker(
  File "/home/eva/.local/lib/python3.9/site-packages/celery/worker/worker.py", line 93, in __init__
    self.app.loader.init_worker()
  File "/home/eva/.local/lib/python3.9/site-packages/celery/loaders/base.py", line 110, in init_worker
    self.import_default_modules()
  File "/home/eva/.local/lib/python3.9/site-packages/celery/loaders/base.py", line 104, in import_default_modules
    raise response
  File "/home/eva/.local/lib/python3.9/site-packages/celery/utils/dispatch/signal.py", line 276, in send
    response = receiver(signal=self, sender=sender, **named)
  File "/home/eva/.local/lib/python3.9/site-packages/celery/fixups/django.py", line 97, in on_import_modules
    self.worker_fixup.validate_models()
  File "/home/eva/.local/lib/python3.9/site-packages/celery/fixups/django.py", line 135, in validate_models
    self.django_setup()
  File "/home/eva/.local/lib/python3.9/site-packages/celery/fixups/django.py", line 131, in django_setup
    django.setup()
  File "/home/eva/.local/lib/python3.9/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/home/eva/.local/lib/python3.9/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/home/eva/.local/lib/python3.9/site-packages/django/apps/config.py", line 193, in create
    import_module(entry)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 984, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'corsheaders'
