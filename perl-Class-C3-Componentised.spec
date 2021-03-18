#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-C3-Componentised
Version  : 1.001002
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-C3-Componentised-1.001002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-C3-Componentised-1.001002.tar.gz
Summary  : 'Load mix-ins or components to your C3-based class'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-C3-Componentised-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
NAME
Class::C3::Componentised - Load mix-ins or components to your C3-based
class

%package dev
Summary: dev components for the perl-Class-C3-Componentised package.
Group: Development
Provides: perl-Class-C3-Componentised-devel = %{version}-%{release}
Requires: perl-Class-C3-Componentised = %{version}-%{release}

%description dev
dev components for the perl-Class-C3-Componentised package.


%package perl
Summary: perl components for the perl-Class-C3-Componentised package.
Group: Default
Requires: perl-Class-C3-Componentised = %{version}-%{release}

%description perl
perl components for the perl-Class-C3-Componentised package.


%prep
%setup -q -n Class-C3-Componentised-1.001002
cd %{_builddir}/Class-C3-Componentised-1.001002

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::C3::Componentised.3
/usr/share/man/man3/Class::C3::Componentised::ApplyHooks.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Class/C3/Componentised.pm
/usr/lib/perl5/vendor_perl/5.32.1/Class/C3/Componentised/ApplyHooks.pm
