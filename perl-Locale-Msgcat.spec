%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Msgcat
Summary:	%{pdir}::%{pnam} perl module
Summary(cs):	Modul %{pdir}::%{pnam} pro Perl
Summary(da):	Perlmodul %{pdir}::%{pnam}
Summary(de):	%{pdir}::%{pnam} Perl Modul
Summary(es):	Módulo de Perl %{pdir}::%{pnam}
Summary(fr):	Module Perl %{pdir}::%{pnam}
Summary(it):	Modulo di Perl %{pdir}::%{pnam}
Summary(ja):	%{pdir}::%{pnam} Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	%{pdir}::%{pnam} ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul %{pdir}::%{pnam}
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Summary(pt_BR):	Módulo Perl %{pdir}::%{pnam}
Summary(pt):	Módulo de Perl %{pdir}::%{pnam}
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(sv):	%{pdir}::%{pnam} Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(zh_CN):	%{pdir}::%{pnam} Perl Ä£¿é
Name:		perl-Locale-Msgcat
Version:	1.03
Release:	7
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://www.cpan.org/
BuildRequires:	perl-devel >= 5.6
Requires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Locale::Msgcat module allows access to the XPG4 message catalog
functions (catopen(3), catgets(3) and catclose(4)), which are available
on some systems.

%description -l pl
Modu³ Locale::Msgcat oferuje dostêp do katalogu komunikatów XPG4 poprzez
funkcje catopen(3), catgets(3) and catclose(4), dostêpne na niektórych
systemach.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL OPTIMIZE="%{rpmcflags}" \
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
