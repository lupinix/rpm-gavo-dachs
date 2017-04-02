# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}


%global srcname tapsh
%global sum tapsh is a simple shell to query TAP servers
%global common_desc The TAP shell lets you query Virtual Observatory TAP \
services in the style of common database shells.


# No Python3 by upstream yet, but spec already supports it in general.
%if 0%{?fedora}
%bcond_with python3
%else
%bcond_with python3
%endif

Name:           python-%{srcname}
Version:        0.7.1
Release:        1%{?dist}
Summary:        %{sum}

License:        GPLv3+
URL:            http://vo.ari.uni-heidelberg.de/soft
Source0:        http://soft.g-vo.org/dist/%{srcname}-%{version}.tar.gz

# We use the sqlite provided by Python, not pysqlite
Patch0:         tapsh-0.7.1-no-pysqlite.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-gavoutils
BuildRequires:  python2-gavovot
BuildRequires:  python-setuptools
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-gavoutils
BuildRequires:  python3-gavovot
BuildRequires:  python3-setuptools
%endif # with python3

%description
%{common_desc}

%package -n %{srcname}
Summary:        %{sum}
Requires:       python2-%{srcname} = %{version}-%{release}

%description -n %{srcname}
%{common_desc}

%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       python2-gavoutils
Requires:       python2-gavovot
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_desc}

%if %{with python3}
%package -n python3-%{srcname}
Summary:      %{sum}
Requires:     python3-gavoutils
Requires:     python3-gavovot
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%endif # with python3


%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py2_build

%if %{with python3}
%py3_build
%endif # with python3


%install
%py2_install

%if %{with python3}
%py3_install
%endif # with python3

%check
%{__python2} setup.py test

%if %{with python3}
%{__python3} setup.py test
%endif

%files -n %{srcname}
%{_bindir}/%{srcname}

%files -n python2-%{srcname}
%doc README
%{python2_sitelib}/*

%if %{with python3}
%files -n python3-%{srcname}
%doc README
%{python3_sitelib}/*
%endif # with python3


%changelog
* Sun Apr  2 2017 Christian Dersch <lupinix@mailbox.org> - 0.7.1-1
- initial packaging effort
