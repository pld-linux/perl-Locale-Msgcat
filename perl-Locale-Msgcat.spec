#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Msgcat
Summary:	Locale::Msgcat - access the XPG4 message catalog functions
Summary(pl.UTF-8):	Locale::Msgcat - dostęp do funkcji katalogów komunikatów XPG4
Name:		perl-Locale-Msgcat
Version:	1.03
Release:	20
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pnam}-%{version}.tar.gz
# Source0-md5:	8dbfee7b81e94cf946c9f28ab0bc5291
URL:		http://search.cpan.org/dist/Locale-Msgcat/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Locale::Msgcat module allows access to the XPG4 message catalog
functions (catopen(3), catgets(3) and catclose(3)), which are
available on some systems.

%description -l pl.UTF-8
Moduł Locale::Msgcat oferuje dostęp do katalogu komunikatów XPG4
poprzez funkcje catopen(3), catgets(3) and catclose(3), dostępne na
niektórych systemach.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Locale/*.pm
%dir %{perl_vendorarch}/auto/Locale/Msgcat
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/Msgcat/*.so
