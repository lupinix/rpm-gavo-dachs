# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}


%global srcname gavostc
%global sum A library for processing IVOA STC information
%global common_desc A library for processing IVOA STC information.


# No Python3 by upstream yet, but spec already supports it in general.
%if 0%{?fedora}
%bcond_with python3
%else
%bcond_with python3
%endif

Name:           python-%{srcname}
Version:        0.9.8
Release:        1%{?dist}
Summary:        %{sum}

License:        GPLv3+
URL:            http://vo.ari.uni-heidelberg.de/soft
Source0:        http://soft.g-vo.org/dist/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-gavoutils
BuildRequires:  python-setuptools
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-gavoutils
BuildRequires:  python3-setuptools
%endif # with python3

%description
%{common_desc}

%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       python2-gavoutils
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_desc}

%if %{with python3}
%package -n python3-%{srcname}
Summary:      %{sum}
Requires:     python3-gavoutils
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%endif # with python3


%prep
%autosetup -n  %{srcname}-%{version}

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


%files -n python2-%{srcname}
%license COPYING
%doc README
%{python2_sitelib}/*

%if %{with python3}
%files -n python3-%{srcname}
%license COPYING
%doc README
%{python3_sitelib}/*
%endif # with python3


%changelog
* Sun Apr  2 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.8-1
- initial packaging effort
