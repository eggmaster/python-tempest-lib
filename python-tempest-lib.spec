%global pypi_name tempest-lib

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Functional Testing Library

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr >= 1.6
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  dos2unix
Requires:  python-babel
Requires:  python-fixtures
Requires:  python-iso8601
Requires:  python-jsonschema
Requires:  python-httplib2
Requires:  python-oslo-context >= 0.2.0
Requires:  python-oslo-log >= 1.8.0
Requires:  python-oslo-config >= 1.9.3
Requires:  python-oslo-utils >= 1.4.0
Requires:  python-oslo-i18n >= 1.5.0
Requires:  python-oslo-serialization >= 1.4.0
Requires:  python-oslo-concurrency >= 1.8.0
Requires:  python2-os-testr >= 0.1.0
Requires:  python-paramiko

%description
Library for creating test suites for OpenStack projects.

%package doc
Summary: Documentation for %{name}
Group: Documentation
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove shebangs and fix permissions
find -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \
   -exec chmod u=rw,go=r {} \;

%build
%{__python2} setup.py build
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
dos2unix html/_static/jquery.js

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst HACKING.rst AUTHORS ChangeLog CONTRIBUTING.rst
%license LICENSE
%{_bindir}/skip-tracker
%{_bindir}/check-uuid
%{python2_sitelib}/tempest_lib
%{python2_sitelib}/tempest_lib-%{upstream_version}-py?.?.egg-info

%files doc
%doc html doc/source/readme.rst

%changelog
* Tue Jan 20 2015 Steve Linabery <slinaber@redhat.com> - 0.0.4-1
- Initial package.
