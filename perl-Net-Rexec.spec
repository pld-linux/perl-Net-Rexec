%include	/usr/lib/rpm/macros.perl
Summary:	Net-Rexec perl module
Summary(pl):	Modu³ perla Net-Rexec
Name:		perl-Net-Rexec
Version:	0.12
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Rexec-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Rexec Perl extension for the REXEC protocol.

%description -l pl
Net-Rexec - wsparcie dla protoko³u REXEC.

%prep
%setup -q -n Net-Rexec-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Rexec.pm
%{_mandir}/man3/*
