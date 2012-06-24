%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Lockf
Summary:	File::lockf - Perl module interface to the lockf system call
Summary(pl):	File::lockf - interfejs perlowy do wywo�ania systemowego lockf
Name:		perl-File-Lockf
Version:	0.20
Release:	9
License:	GPL v1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b200cf22e08f12d678a1c83312ff4f5d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-lockf is an interface to the lockf system call.  Perl supports
the flock system call natively, but that does not acquire network
locks. Perl also supports the fcntl system call, but that is somewhat
ugly to use.  There are other locking modules available for Perl, but
none of them provided a simple, clean interface to the lockf system
call, without any bells or whistles getting in the way.

%description -l pl
File::lockf stanowi interfejs do wywo�ania systemowego lockf. Perl
posiada wbudowan� obs�ug� lockf, ale nie wspiera ona blokad
sieciowych. Istniej� inne modu�y Perla do zak�adania blokad, ale �aden
z nich nie posiada prostego, jasnego interfejsu do wywo�ania
systemowego lockf bez �adnych dzwonk�w i gwizdk�w po drodze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/File/lockf.pm
%dir %{perl_vendorarch}/auto/File/lockf
%{perl_vendorarch}/auto/File/lockf/lockf.bs
%attr(755,root,root) %{perl_vendorarch}/auto/File/lockf/lockf.so
%{_mandir}/man3/*
