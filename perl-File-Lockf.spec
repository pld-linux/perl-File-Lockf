%include	/usr/lib/rpm/macros.perl
Summary:	File-Lockf perl module
Summary(pl):	Modu� perla File-Lockf
Name:		perl-File-Lockf
Version:	0.20
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Lockf-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Lockf is a wrapper around the lockf system call.

%description -l pl
File-Lockf umo�liwia korzystanie z wywo�ania systemowego lockf.

%prep
%setup -q -n File-Lockf-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/File/lockf/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/lockf
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/File/lockf.pm

%dir %{perl_sitearch}/auto/File/lockf
%{perl_sitearch}/auto/File/lockf/.packlist
%{perl_sitearch}/auto/File/lockf/lockf.bs
%attr(755,root,root) %{perl_sitearch}/auto/File/lockf/lockf.so

%{_mandir}/man3/*
