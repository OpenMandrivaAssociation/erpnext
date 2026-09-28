Summary:	Open source ERP and accounting
Name:		erpnext
# The typelib generator greps every .js and .py. This tree does not
# ship GObject typelibs, and node_modules makes that scan dominate the build.
%global __typelib_path ^$
%global debug_package %{nil}
# Upstream pins are for the bench installer. The system copies of those
# modules are what we run against.
%global __requires_exclude_from /(frappe|erpnext)-.*dist-info/METADATA$
%global __requires_exclude ^python3(\\.14)?dist\\((psycopg2-binary|ipython|barcodenumber|pypdfium2)\\)
# ERPNext 16.36.0 (GPLv3) with the Frappe 16.35.0 framework (MIT).
# Dependencies are system packages. pypdfium2 is not packaged: its build
# downloads prebuilt pdfium binaries.
Version:	16.36.0
Release:	1
License:	GPL-3.0-or-later AND MIT
Group:		Applications/Productivity
URL:		https://frappe.io/erpnext
Source0:	erpnext-%{version}-apps.tar.xz
Source2:	common_site_config.json
Source3:	erpnext.sysusers
Source4:	README.install.omv
Source5:	assets.json
Source6:	assets-rtl.json
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(bleach-allowlist)
BuildRequires:	python%{pyver}dist(dataclasses-json)
BuildRequires:	python%{pyver}dist(duckdb)
BuildRequires:	python%{pyver}dist(email-reply-parser)
BuildRequires:	python%{pyver}dist(googlemaps)
BuildRequires:	python%{pyver}dist(gunicorn)
BuildRequires:	python%{pyver}dist(hiredis)
BuildRequires:	python%{pyver}dist(holidays)
BuildRequires:	python%{pyver}dist(markdown2)
BuildRequires:	python%{pyver}dist(mt-940)
BuildRequires:	python%{pyver}dist(num2words)
BuildRequires:	python%{pyver}dist(openpyxl)
BuildRequires:	python%{pyver}dist(pdfkit)
BuildRequires:	python%{pyver}dist(pdfplumber)
BuildRequires:	python%{pyver}dist(plaid-python)
BuildRequires:	python%{pyver}dist(premailer)
BuildRequires:	python%{pyver}dist(pydyf)
BuildRequires:	python%{pyver}dist(pymysql)
BuildRequires:	python%{pyver}dist(pyphen)
BuildRequires:	python%{pyver}dist(pypika)
BuildRequires:	python%{pyver}dist(pyqrcode)
BuildRequires:	python%{pyver}dist(python-youtube)
BuildRequires:	python%{pyver}dist(rauth)
BuildRequires:	python%{pyver}dist(restrictedpython)
BuildRequires:	python%{pyver}dist(rq)
BuildRequires:	python%{pyver}dist(sql-metadata)
BuildRequires:	python%{pyver}dist(sqlglot)
BuildRequires:	python%{pyver}dist(terminaltables)
BuildRequires:	python%{pyver}dist(tinyhtml5)
BuildRequires:	python%{pyver}dist(traceback-with-variables)
BuildRequires:	python%{pyver}dist(typing-inspect)
BuildRequires:	python%{pyver}dist(vobject)
BuildRequires:	python%{pyver}dist(weasyprint)
BuildRequires:	python%{pyver}dist(xlsxwriter)
BuildRequires:	python%{pyver}dist(zxcvbn)
Requires:	nodejs
Requires:	python
Requires:	python%{pyver}dist(babel)
Requires:	python%{pyver}dist(beautifulsoup4)
Requires:	python%{pyver}dist(cryptography)
Requires:	python%{pyver}dist(cssutils)
Requires:	python%{pyver}dist(croniter)
Requires:	python%{pyver}dist(python-dateutil)
Requires:	python%{pyver}dist(filetype)
Requires:	python%{pyver}dist(gitpython)
Requires:	python%{pyver}dist(jinja2)
Requires:	python%{pyver}dist(python-ldap)
Requires:	python%{pyver}dist(markdownify)
Requires:	python%{pyver}dist(mysqlclient)
Requires:	python%{pyver}dist(nh3)
Requires:	python%{pyver}dist(orjson)
Requires:	python%{pyver}dist(passlib)
Requires:	python%{pyver}dist(pdfminer.six)
Requires:	python%{pyver}dist(phonenumbers)
Requires:	python%{pyver}dist(pillow)
Requires:	python%{pyver}dist(psutil)
Requires:	python%{pyver}dist(psycopg2)
Requires:	python%{pyver}dist(pyarrow)
Requires:	python%{pyver}dist(pycountry)
Requires:	python%{pyver}dist(pydantic)
Requires:	python%{pyver}dist(pyjwt)
Requires:	python%{pyver}dist(pyopenssl)
Requires:	python%{pyver}dist(pyotp)
Requires:	python%{pyver}dist(pypdf)
Requires:	python%{pyver}dist(pypng)
Requires:	python%{pyver}dist(pyyaml)
Requires:	python%{pyver}dist(rapidfuzz)
Requires:	python%{pyver}dist(redis)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(sentry-sdk)
Requires:	python%{pyver}dist(sqlparse)
Requires:	python%{pyver}dist(tenacity)
Requires:	python%{pyver}dist(bleach-allowlist)
Requires:	python%{pyver}dist(dataclasses-json)
Requires:	python%{pyver}dist(duckdb)
Requires:	python%{pyver}dist(email-reply-parser)
Requires:	python%{pyver}dist(googlemaps)
Requires:	python%{pyver}dist(gunicorn)
Requires:	python%{pyver}dist(hiredis)
Requires:	python%{pyver}dist(holidays)
Requires:	python%{pyver}dist(markdown2)
Requires:	python%{pyver}dist(mt-940)
Requires:	python%{pyver}dist(num2words)
Requires:	python%{pyver}dist(openpyxl)
Requires:	python%{pyver}dist(pdfkit)
Requires:	python%{pyver}dist(pdfplumber)
Requires:	python%{pyver}dist(plaid-python)
Requires:	python%{pyver}dist(premailer)
Requires:	python%{pyver}dist(pydyf)
Requires:	python%{pyver}dist(pymysql)
Requires:	python%{pyver}dist(pyphen)
Requires:	python%{pyver}dist(pypika)
Requires:	python%{pyver}dist(pyqrcode)
Requires:	python%{pyver}dist(python-youtube)
Requires:	python%{pyver}dist(rauth)
Requires:	python%{pyver}dist(restrictedpython)
Requires:	python%{pyver}dist(rq)
Requires:	python%{pyver}dist(sql-metadata)
Requires:	python%{pyver}dist(sqlglot)
Requires:	python%{pyver}dist(terminaltables)
Requires:	python%{pyver}dist(tinyhtml5)
Requires:	python%{pyver}dist(traceback-with-variables)
Requires:	python%{pyver}dist(typing-inspect)
Requires:	python%{pyver}dist(vobject)
Requires:	python%{pyver}dist(weasyprint)
Requires:	python%{pyver}dist(xlsxwriter)
Requires:	python%{pyver}dist(zxcvbn)
Requires:	python%{pyver}dist(unidecode)
Requires:	python%{pyver}dist(websockets)
Requires:	python%{pyver}dist(werkzeug)
Requires:	python%{pyver}dist(whoosh-reloaded)
Requires:	python%{pyver}dist(xlrd)
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

%build
# Local wheels only. Dependencies are already installed BuildRequires.
mkdir -p %{_builddir}/wheels
pip wheel --wheel-dir %{_builddir}/wheels --no-deps --no-build-isolation --no-index \
	apps/frappe apps/erpnext

%install
pip install --root %{buildroot} --no-deps --no-index --no-cache-dir \
	--find-links %{_builddir}/wheels %{_builddir}/wheels/*.whl

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
exec /usr/bin/python -m frappe.utils.bench_helper frappe "$@"
EOF
chmod 0755 %{buildroot}/usr/bin/erpnext

install -d %{buildroot}/var/lib/erpnext/sites/assets
cp %{SOURCE2} %{buildroot}/var/lib/erpnext/sites/common_site_config.json
printf 'frappe\nerpnext\n' > %{buildroot}/var/lib/erpnext/sites/apps.txt
cp %{SOURCE5} %{SOURCE6} %{buildroot}/var/lib/erpnext/sites/assets/
frappe_public=$(find %{buildroot}%{python_sitelib} -type d -path '*/frappe/public' | head -1)
erpnext_public=$(find %{buildroot}%{python_sitelib} -type d -path '*/erpnext/public' | head -1)
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
ExecStart=/usr/bin/python -m gunicorn --bind 127.0.0.1:8000 --workers 2 --timeout 120 frappe.app:application
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
%{python_sitelib}/frappe
%{python_sitelib}/frappe-*.dist-info
%{python_sitelib}/erpnext
%{python_sitelib}/erpnext-*.dist-info
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
