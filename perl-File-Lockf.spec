%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Lockf
Summary:	File::Lockf perl module
Summary(pl):	Modu³ perla File::Lockf
Name:		perl-File-Lockf
Version:	0.20
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Lockf is a wrapper around the lockf system call.

%description -l pl
File::Lockf umo¿liwia korzystanie z wywo³ania systemowego lockf.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/File/lockf.pm
%dir %{perl_sitearch}/auto/File/lockf
%{perl_sitearch}/auto/File/lockf/lockf.bs
%attr(755,root,root) %{perl_sitearch}/auto/File/lockf/lockf.so
%{_mandir}/man3/*
