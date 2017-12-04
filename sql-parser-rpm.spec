Name:           sql-parser
Version:        %{VERSION}
Release:        1%{?dist}
Summary:        SQL Parser for C++. Building C++ object structure from SQL statements.
Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/hyrise/sql-parser
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc-c++ 


%description
This is a SQL Parser for C++. It parses the given SQL query into C++ objects

%package devel
Summary:	%{name} c++ development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
C++ Development files for %{name}.

%prep
%setup -n %{name}-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib
make install INSTALL=$RPM_BUILD_ROOT/usr
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64

mkdir -p $RPM_BUILD_ROOT/usr/include/hsql/sql
cp src/*.h $RPM_BUILD_ROOT/usr/include/hsql
cp src/sql/*.h $RPM_BUILD_ROOT/usr/include/hsql/sql

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc README.md LICENSE docs
%{_libdir}/libsqlparser.so

%files devel
%defattr(-,root,root,-)
%{_includedir}

%changelog
