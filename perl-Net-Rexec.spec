#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Rexec
Summary:	Net::Rexec perl module
Summary(pl):	Modu³ perla Net::Rexec
Name:		perl-Net-Rexec
Version:	0.12
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e6309fb4eaa25c75f9463dc769da42d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Rexec Perl extension for the REXEC protocol.

%description -l pl
Net::Rexec - wsparcie dla protoko³u REXEC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/Rexec.pm
%{_mandir}/man3/*
