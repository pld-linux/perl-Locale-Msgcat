%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Msgcat
Summary:	Locale::Msgcat - access the XPG4 message catalog functions
Summary(pl):	Locale::Msgcat - dostêp do funkcji katalogów komunikatów XPG4
Name:		perl-Locale-Msgcat
Version:	1.03
Release:	7
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	8dbfee7b81e94cf946c9f28ab0bc5291
URL:		http://www.cpan.org/
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Locale::Msgcat module allows access to the XPG4 message catalog
functions (catopen(3), catgets(3) and catclose(3)), which are
available on some systems.

%description -l pl
Modu³ Locale::Msgcat oferuje dostêp do katalogu komunikatów XPG4
poprzez funkcje catopen(3), catgets(3) and catclose(3), dostêpne na
niektórych systemach.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	OPTIMIZE="%{rpmcflags}" \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Locale/*.pm
%dir %{perl_vendorarch}/auto/Locale/Msgcat
%{perl_vendorarch}/auto/Locale/Msgcat/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/Msgcat/*.so
