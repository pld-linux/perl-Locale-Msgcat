%include	/usr/lib/rpm/macros.perl
Summary:	Msgcat module for perl (Locale)
Summary(pl):	Modu³ perla Msgcat
Name:		perl-Locale-Msgcat
Version:	1.03
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Locale/Msgcat-%{version}.tar.gz
URL:		http://www.cpan.org/
BuildRequires:	perl >= 5.6
Requires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Msgcat module for perl.

%description -l pl
Modu³ perla Msgcat.

%prep
%setup -q -n Msgcat-%{version} 

%build
CFLAGS="%{rpmcflags}" perl Makefile.PL
%{__make}

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{perl_sitearch}/Locale/*.pm
%dir %{perl_sitearch}/auto/Locale/Msgcat
%{perl_sitearch}/auto/Locale/Msgcat/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Locale/Msgcat/*.so
