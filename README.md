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
