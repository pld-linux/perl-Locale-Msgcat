%include	/usr/lib/rpm/macros.perl
Summary:	Msgcat module for perl (Locale)
Name:		perl-Locale-Msgcat
Version:	1.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-authors/id/CHRWOLF/Msgcat-%{version}.tar.gz
URL:		http://www.cpan.org/
BuildRequires:	perl >= 5.6
Requires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Msgcat module for perl.

%prep
%setup -q -n Msgcat-%{version} 

%build
CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" perl Makefile.PL
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
