Summary:	Open source ERP and accounting
Name:		erpnext
# The typelib generator greps every .js and .py. This tree does not
# ship GObject typelibs, and node_modules makes that scan dominate the build.
%global __typelib_path ^$
%global debug_package %{nil}
# Upstream pins are for the bench installer. The system copies of those
# modules are newer or older than the pin and are what we run against.
# Drop upstream version pins. The auto generator turns pyproject
# Requires-Dist into exact ranges the system packages do not satisfy.
%global __requires_exclude_from ^/usr/lib/erpnext/
# ERPNext 16.36.0 (GPLv3) with the Frappe 16.35.0 framework (MIT) it requires.
# Python packages missing from the distribution are vendored as source
# tarballs and compiled during the build. psycopg2-binary is not used;
# the system psycopg2 module is. pypdfium2 is not packaged: its build
# downloads prebuilt pdfium binaries.
Version:	16.36.0
Release:	1
License:	GPL-3.0-or-later AND MIT
Group:		Applications/Productivity
URL:		https://frappe.io/erpnext
Source0:	erpnext-%{version}-apps.tar.xz
Source1:	erpnext-%{version}-sdists.tar.xz
Source2:	common_site_config.json
Source3:	erpnext.sysusers
Source4:	README.install.omv
Source5:	assets.json
Source6:	assets-rtl.json
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	lib64python-devel
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(libmariadb)
BuildRequires:	python-dunamai
BuildRequires:	python-pip
BuildRequires:	python-setuptools
Requires:	nodejs
Requires:	python
Requires:	python-babel
Requires:	python-beautifulsoup4
Requires:	python-cryptography
Requires:	python-cssutils
Requires:	python-croniter
Requires:	python-dateutil
Requires:	python-filetype
Requires:	python-gitpython
Requires:	python-jinja2
Requires:	python-ldap
Requires:	python-markdownify
Requires:	python-mysql
Requires:	python-nh3
Requires:	python-orjson
Requires:	python-passlib
Requires:	python-pdfminer
Requires:	python-phonenumbers
Requires:	python-pillow
Requires:	python-psutil
Requires:	python-psycopg2
Requires:	python-pyarrow
Requires:	python-pycountry
Requires:	python-pydantic
Requires:	python-pyjwt
Requires:	python-pyopenssl
Requires:	python-pyotp
Requires:	python-pypdf
Requires:	python-pypng
Requires:	python-pyyaml
Requires:	python-rapidfuzz
Requires:	python-redis
Requires:	python-requests
Requires:	python-sentry-sdk
Requires:	python-tenacity
Requires:	python-unidecode
Requires:	python-websockets
Requires:	python-werkzeug
Requires:	python-whoosh
Requires:	python-xlrd
Requires:	redis
Recommends:	mariadb-server
%description
ERPNext is an ERP with accounting, invoicing, inventory, sales, and
purchases, built on the Frappe framework. This package is the GPLv3
application and the MIT-licensed framework it runs on.

The web service listens on 127.0.0.1:8000. MariaDB is expected on the
local host, and Redis runs as three private Unix-socket instances.
See README.install.omv after installation.

%package nginx
Summary:	nginx reverse proxy for ERPNext
Group:		Applications/Productivity
Requires:	%{name} = %{EVRD}
Requires:	nginx

%description nginx
nginx site that proxies erpnext.* to ERPNext on port 8000 and to the
realtime service on port 9000. The site is installed disabled.

%prep
%autosetup -c -T -D
tar -xf %{SOURCE0}
tar -xf %{SOURCE1}

%build

%install
python -m venv --system-site-packages --without-pip %{buildroot}/usr/lib/erpnext/venv
/usr/bin/pip --python %{buildroot}/usr/lib/erpnext/venv/bin/python install --no-binary :all: --no-index \
	--find-links sdists --no-build-isolation \
	poetry-dynamic-versioning
/usr/bin/pip --python %{buildroot}/usr/lib/erpnext/venv/bin/python install --no-binary :all: --no-index \
	--find-links sdists --no-build-isolation \
	'PyMySQL==1.1.2' 'PyQRCode~=1.2.1' 'RestrictedPython~=8.1' \
	'WeasyPrint==68.0' 'pydyf==0.12.1' 'bleach-allowlist~=1.0.3' \
	'email-reply-parser~=0.5.12' 'markdown2~=2.5.4' 'num2words~=0.5.14' \
	'openpyxl~=3.1.5' 'xlsxwriter~=3.2.9' 'pdfkit~=1.0.0' \
	'premailer~=3.10.0' 'rauth~=0.7.3' 'hiredis~=3.3.0' 'rq==2.6.1' \
	'sql_metadata~=3.0.1' 'sqlparse~=0.6.0' 'terminaltables~=3.1.10' \
	'traceback-with-variables~=2.2.1' 'zxcvbn~=4.5.0' 'holidays~=0.87' \
	'googlemaps~=4.10.0' 'plaid-python~=7.2.1' 'python-youtube~=0.9.9' \
	'mt-940==4.30.0' 'vobject~=0.9.9' 'duckdb~=1.4.3' \
	sdists/pypika-*.tar.gz sdists/gunicorn-*.tar.gz
/usr/bin/pip --python %{buildroot}/usr/lib/erpnext/venv/bin/python install --no-binary :all: --no-index \
	--find-links sdists --no-build-isolation --no-deps \
	pdfplumber
/usr/bin/pip --python %{buildroot}/usr/lib/erpnext/venv/bin/python install --no-deps --no-build-isolation \
	apps/frappe apps/erpnext
find %{buildroot}/usr/lib/erpnext/venv/bin -type f -exec \
	sed -i '1s|^#!.*python.*|#!/usr/lib/erpnext/venv/bin/python|' {} +

install -d %{buildroot}/usr/lib/erpnext
cp -a apps %{buildroot}/usr/lib/erpnext/apps
# Yarn downloaded prebuilt esbuild and socket.io accelerators. Runtime
# uses Node's pure JavaScript paths. Do not ship those binaries.
rm -rf %{buildroot}/usr/lib/erpnext/apps/frappe/node_modules/esbuild-linux-64
rm -rf %{buildroot}/usr/lib/erpnext/apps/frappe/node_modules/@esbuild
find %{buildroot}/usr/lib/erpnext/apps -type d -name prebuilds -exec rm -rf {} + || :
ln -s /var/lib/erpnext/sites %{buildroot}/usr/lib/erpnext/sites

install -d %{buildroot}/usr/bin
cat > %{buildroot}/usr/bin/erpnext << 'EOF'
#!/bin/sh
export FRAPPE_BENCH_ROOT=/usr/lib/erpnext
cd /var/lib/erpnext/sites || exit 1
exec /usr/lib/erpnext/venv/bin/python -m frappe.utils.bench_helper frappe "$@"
EOF
chmod 0755 %{buildroot}/usr/bin/erpnext

install -d %{buildroot}/var/lib/erpnext/sites/assets
cp %{SOURCE2} %{buildroot}/var/lib/erpnext/sites/common_site_config.json
printf 'frappe\nerpnext\n' > %{buildroot}/var/lib/erpnext/sites/apps.txt
cp %{SOURCE5} %{SOURCE6} %{buildroot}/var/lib/erpnext/sites/assets/
frappe_public=$(find %{buildroot}/usr/lib/erpnext/venv -type d -path '*/site-packages/frappe/public' | head -1)
erpnext_public=$(find %{buildroot}/usr/lib/erpnext/venv -type d -path '*/site-packages/erpnext/public' | head -1)
ln -s "${frappe_public#%{buildroot}}" %{buildroot}/var/lib/erpnext/sites/assets/frappe
ln -s "${erpnext_public#%{buildroot}}" %{buildroot}/var/lib/erpnext/sites/assets/erpnext

install -d %{buildroot}/var/log/erpnext
install -d %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/erpnext.conf

install -d %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/erpnext.conf << 'EOF'
d /var/lib/erpnext 0750 erpnext erpnext -
d /var/lib/erpnext/sites 0750 erpnext erpnext -
d /var/log/erpnext 0750 erpnext erpnext -
d /srv/redis/erpnext-cache 0750 redis redis -
d /srv/redis/erpnext-queue 0750 redis redis -
d /srv/redis/erpnext-socketio 0750 redis redis -
EOF

install -d %{buildroot}%{_sysconfdir}/redis
for inst in erpnext-cache erpnext-queue erpnext-socketio; do
	cat > %{buildroot}%{_sysconfdir}/redis/${inst}.conf << EOF
# redis@${inst} — private instance for ERPNext
bind 127.0.0.1 -::1
protected-mode yes
port 0
unixsocket /run/redis/${inst}/redis.sock
unixsocketperm 666
pidfile /run/redis/${inst}.pid
dir /srv/redis/${inst}
dbfilename dump.rdb
logfile ""
loglevel notice
daemonize no
supervised systemd
timeout 0
tcp-keepalive 300
EOF
done

install -d %{buildroot}%{_unitdir}/multi-user.target.wants
for inst in erpnext-cache erpnext-queue erpnext-socketio; do
	ln -s ../redis@.service %{buildroot}%{_unitdir}/multi-user.target.wants/redis@${inst}.service
done

cat > %{buildroot}%{_unitdir}/erpnext.service << 'EOF'
[Unit]
Description=ERPNext web
After=network.target mariadb.service redis@erpnext-cache.service redis@erpnext-queue.service
Wants=mariadb.service redis@erpnext-cache.service redis@erpnext-queue.service

[Service]
Type=simple
User=erpnext
Group=erpnext
Environment=FRAPPE_BENCH_ROOT=/usr/lib/erpnext
WorkingDirectory=/var/lib/erpnext/sites
ExecStart=/usr/lib/erpnext/venv/bin/gunicorn --bind 127.0.0.1:8000 --workers 2 --timeout 120 frappe.app:application
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

cat > %{buildroot}%{_unitdir}/erpnext-worker.service << 'EOF'
[Unit]
Description=ERPNext background jobs
After=network.target erpnext.service redis@erpnext-queue.service
Wants=redis@erpnext-queue.service

[Service]
Type=simple
User=erpnext
Group=erpnext
Environment=FRAPPE_BENCH_ROOT=/usr/lib/erpnext
ExecStart=/usr/bin/erpnext worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

cat > %{buildroot}%{_unitdir}/erpnext-scheduler.service << 'EOF'
[Unit]
Description=ERPNext scheduler
After=network.target erpnext.service redis@erpnext-queue.service
Wants=redis@erpnext-queue.service

[Service]
Type=simple
User=erpnext
Group=erpnext
Environment=FRAPPE_BENCH_ROOT=/usr/lib/erpnext
ExecStart=/usr/bin/erpnext schedule
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

cat > %{buildroot}%{_unitdir}/erpnext-socketio.service << 'EOF'
[Unit]
Description=ERPNext realtime
After=network.target redis@erpnext-socketio.service redis@erpnext-queue.service
Wants=redis@erpnext-socketio.service redis@erpnext-queue.service

[Service]
Type=simple
User=erpnext
Group=erpnext
Environment=FRAPPE_BENCH_ROOT=/usr/lib/erpnext
WorkingDirectory=/usr/lib/erpnext/apps/frappe
ExecStart=/usr/bin/node /usr/lib/erpnext/apps/frappe/socketio.js
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

install -d %{buildroot}%{_sysconfdir}/nginx/sites-available
cat > %{buildroot}%{_sysconfdir}/nginx/sites-available/erpnext.conf << 'EOF'
upstream erpnext {
	server 127.0.0.1:8000;
}

upstream erpnext_socketio {
	server 127.0.0.1:9000;
}

server {
	listen 80;
	server_name erpnext.*;

	proxy_read_timeout 720s;
	proxy_connect_timeout 720s;
	proxy_send_timeout 720s;
	client_max_body_size 50m;

	location /socket.io {
		proxy_pass http://erpnext_socketio;
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection "upgrade";
		proxy_set_header Host $host;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_set_header X-Real-IP $remote_addr;
	}

	location / {
		proxy_pass http://erpnext;
		proxy_set_header Host $host;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_set_header X-Real-IP $remote_addr;
	}
}
EOF

cp %{SOURCE4} .

%files
%doc README.install.omv
%dir /usr/lib/erpnext
/usr/lib/erpnext/venv
/usr/lib/erpnext/apps
/usr/lib/erpnext/sites
/usr/bin/erpnext
%dir %attr(0750,erpnext,erpnext) /var/lib/erpnext
%dir %attr(0750,erpnext,erpnext) /var/lib/erpnext/sites
%attr(0640,root,erpnext) %config(noreplace) /var/lib/erpnext/sites/common_site_config.json
%config(noreplace) /var/lib/erpnext/sites/apps.txt
%dir /var/lib/erpnext/sites/assets
%config(noreplace) /var/lib/erpnext/sites/assets/assets.json
%config(noreplace) /var/lib/erpnext/sites/assets/assets-rtl.json
/var/lib/erpnext/sites/assets/frappe
/var/lib/erpnext/sites/assets/erpnext
%dir %attr(0750,erpnext,erpnext) /var/log/erpnext
%{_unitdir}/erpnext.service
%{_unitdir}/erpnext-worker.service
%{_unitdir}/erpnext-scheduler.service
%{_unitdir}/erpnext-socketio.service
%{_unitdir}/multi-user.target.wants/redis@erpnext-cache.service
%{_unitdir}/multi-user.target.wants/redis@erpnext-queue.service
%{_unitdir}/multi-user.target.wants/redis@erpnext-socketio.service
%config(noreplace) %attr(0640,root,redis) %{_sysconfdir}/redis/erpnext-cache.conf
%config(noreplace) %attr(0640,root,redis) %{_sysconfdir}/redis/erpnext-queue.conf
%config(noreplace) %attr(0640,root,redis) %{_sysconfdir}/redis/erpnext-socketio.conf
%{_sysusersdir}/erpnext.conf
%{_tmpfilesdir}/erpnext.conf

%files nginx
%config(noreplace) %{_sysconfdir}/nginx/sites-available/erpnext.conf
