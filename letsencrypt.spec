%global         revision d045f7c
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           letsencrypt
Version:        0
Release:        1.git%{revision}%{?dist}
Summary:        A free, automated certificate authority


License:        ASL
URL:            https://letsencrypt.org/
Source0:        %{name}-%{revision}.tar.xz

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools

Requires:       python-cryptography python-setuptools python-zope-interface
Requires:       python-zope-component pytz python-psutil python-mock
Requires:       python-configobj python-werkzeug python-ndg_httpsclient
Requires:       pyOpenSSL

# pip install python2-pythondialog>=3.2.2rc1
# pip install pyrfc3339 parsedatetime ConfigArgParse argparse

%description
Let's Encrypt is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%prep
%setup -q -n %{name}-%{revision}


%build
(cd acme && CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build)
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
(cd acme && %{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT)
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc LICENSE.txt
%{python_sitelib}/*
%{_bindir}/jws
%{_bindir}/letsencrypt
%{_bindir}/letsencrypt-renewer

%changelog
* Sun Apr 26 2015 Torrie Fischer <tdfischer@hackerbots.net> 0-1.git1d8281d.fc20
- Initial package
