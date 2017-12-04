Name:           sql-parser
Version:	%{VERSION}
Release:        1%{?dist}
Summary:	This is a SQL Parser for C++.
License:	MIT
URL:		https://github.com/hyrise/sql-parser
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	bison

%description
This is a SQL Parser for C++.

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make
mkdir -p $RPM_BUILD_ROOT/usr/lib64/
cp libsqlparser.so $RPM_BUILD_ROOT/usr/lib64/
mkdir -p $RPM_BUILD_ROOT/usr/include/sqlparser
cd src && cp -r * $RPM_BUILD_ROOT/usr/include/sqlparser
find $RPM_BUILD_ROOT/usr/include/sqlparser -not -name '*.h' -type f | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_libdir}/*.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}

%changelog
