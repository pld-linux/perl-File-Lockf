%include	/usr/lib/rpm/macros.perl
Summary:	File-Lockf perl module
Summary(pl):	Modu³ perla File-Lockf
Name:		perl-File-Lockf
Version:	0.20
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Lockf-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Lockf is a wrapper around the lockf system call.

%description -l pl
File-Lockf umo¿liwia korzystanie z wywo³ania systemowego lockf.

%prep
%setup -q -n File-Lockf-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/File/lockf.pm
%dir %{perl_sitearch}/auto/File/lockf
%{perl_sitearch}/auto/File/lockf/lockf.bs
%attr(755,root,root) %{perl_sitearch}/auto/File/lockf/lockf.so
%{_mandir}/man3/*
