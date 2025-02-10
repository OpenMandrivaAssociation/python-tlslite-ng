Name:		python-tlslite-ng
Version:	0.8.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/tlslite-ng/tlslite_ng-%{version}.tar.gz
Summary:	Pure python implementation of SSL and TLS.
URL:		https://pypi.org/project/tlslite-ng/
License:	LGPLv2
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Pure python implementation of SSL and TLS.

%files
%{_bindir}/tls.py
%{_bindir}/tlsdb.py
%{py_sitedir}/tlslite
%{py_sitedir}/tlslite_ng-*.*-info
