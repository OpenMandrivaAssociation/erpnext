Summary:	Open source ERP and accounting
Name:		erpnext
%global __typelib_path ^$
%global debug_package %{nil}
%global __requires_exclude_from /erpnext-.*\\.dist-info$
%global __requires_exclude ^python3(\\.14)?dist\\((barcodenumber|pypdfium2)\\)
# ERPNext 16.36 requires Frappe >= 16.21 and < 17. Frappe is a separate
# package because the framework is used without ERPNext.
Version:	16.36.0
Release:	1
License:	GPL-3.0-or-later
Group:		Applications/Productivity
URL:		https://frappe.io/erpnext
Source0:	erpnext-%{version}-app.tar.xz
Source1:	assets-erpnext.json
Source2:	assets-rtl-erpnext.json
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(frappe)
BuildRequires:	python%{pyver}dist(googlemaps)
BuildRequires:	python%{pyver}dist(holidays)
BuildRequires:	python%{pyver}dist(mt-940)
BuildRequires:	python%{pyver}dist(pdfplumber)
BuildRequires:	python%{pyver}dist(plaid-python)
BuildRequires:	python%{pyver}dist(pypng)
BuildRequires:	python%{pyver}dist(python-youtube)
BuildRequires:	python%{pyver}dist(rapidfuzz)
BuildRequires:	python%{pyver}dist(unidecode)
Requires:	frappe >= 16.21.0
Conflicts:	frappe >= 17
Requires:	python%{pyver}dist(frappe)
Requires:	python%{pyver}dist(googlemaps)
Requires:	python%{pyver}dist(holidays)
Requires:	python%{pyver}dist(mt-940)
Requires:	python%{pyver}dist(pdfplumber)
Requires:	python%{pyver}dist(plaid-python)
Requires:	python%{pyver}dist(pypng)
Requires:	python%{pyver}dist(python-youtube)
Requires:	python%{pyver}dist(rapidfuzz)
Requires:	python%{pyver}dist(unidecode)
%description
ERPNext is an ERP with accounting, invoicing, inventory, sales, and
purchases. It is an application on the Frappe framework, which is the
separate frappe package. Installing this package makes ERPNext available
to a Frappe site; create the site with "frappe new-site --install-app erpnext".

%prep
%autosetup -c -T -D
tar -xf %{SOURCE0}

%build
mkdir -p %{_builddir}/wheels
pip wheel --wheel-dir %{_builddir}/wheels --no-deps --no-build-isolation --no-index \
	./erpnext

%install
pip install --root %{buildroot} --no-deps --no-index --no-cache-dir \
	--find-links %{_builddir}/wheels %{_builddir}/wheels/*.whl

install -d %{buildroot}/var/lib/frappe/sites/assets
cp %{SOURCE1} %{buildroot}/var/lib/frappe/sites/assets/assets-erpnext.json
cp %{SOURCE2} %{buildroot}/var/lib/frappe/sites/assets/assets-rtl-erpnext.json
erpnext_public=$(find %{buildroot}%{python_sitelib} -type d -path '*/erpnext/public' | head -1)
ln -s "${erpnext_public#%{buildroot}}" %{buildroot}/var/lib/frappe/sites/assets/erpnext

%post
if [ -f /var/lib/frappe/sites/apps.txt ] && ! grep -qx erpnext /var/lib/frappe/sites/apps.txt; then
	echo erpnext >> /var/lib/frappe/sites/apps.txt
fi

%postun
if [ "$1" = 0 ] && [ -f /var/lib/frappe/sites/apps.txt ]; then
	grep -vx erpnext /var/lib/frappe/sites/apps.txt > /var/lib/frappe/sites/apps.txt.new || :
	mv /var/lib/frappe/sites/apps.txt.new /var/lib/frappe/sites/apps.txt
fi

%files
%{python_sitelib}/erpnext
%{python_sitelib}/erpnext-*.dist-info
%config(noreplace) /var/lib/frappe/sites/assets/assets-erpnext.json
%config(noreplace) /var/lib/frappe/sites/assets/assets-rtl-erpnext.json
/var/lib/frappe/sites/assets/erpnext
