%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Lockf
Summary:	File::Lockf perl module
Summary(pl):	Modu� perla File::Lockf
Name:		perl-File-Lockf
Version:	0.20
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b200cf22e08f12d678a1c83312ff4f5d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Lockf is a wrapper around the lockf system call.

%description -l pl
File::Lockf umo�liwia korzystanie z wywo�ania systemowego lockf.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
