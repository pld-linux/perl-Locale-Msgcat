%include	/usr/lib/rpm/macros.perl
Summary:	Msgcat module for perl (Locale)
Name:		perl-Locale-Msgcat
Version:	1.03
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	Msgcat-%{version}.tar.gz
Url:		http://www.cpan.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	perl >= 5.6
Requires:	perl >= 5.6

%description
Msgcat module for perl

%prep
%setup -q -n Msgcat-%{version} 

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
%{__make}

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
install -d $RPM_BUILD_ROOT/$installarchlib
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install

[ -x %{_libdir}/rpm/brp-compress ] && %{_libdir}/rpm/brp-compress

find $RPM_BUILD_ROOT%{_prefix} -type f -print |
	sed "s@^$RPM_BUILD_ROOT@@g" | 
	grep -v perllocal.pod | 
	grep -v "\.packlist" > Msgcat-1.03-filelist
if [ "$(cat Msgcat-1.03-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%files 
%defattr(644,root,root,755)
%{perl_sitearch}/Locale/*.pm
%dir %{perl_sitearch}/auto/Locale/Msgcat
%{perl_sitearch}/auto/Locale/Msgcat/*
