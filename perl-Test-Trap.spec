#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	Trap
Summary:	Test::Trap - Trap exit codes, exceptions, output, etc.
Summary(pl.UTF-8):	Test::Trap - przechwytywanie kodów wyjścia, wyjątków, wyjścia itp.
Name:		perl-Test-Trap
Version:	0.3.4
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	7cb432fcb7b8f761e9cc2fc12e76b80b
URL:		https://metacpan.org/release/Test-Trap
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Data-Dump
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Tester >= 0.107
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Primarily (but not exclusively) for use in test scripts: A block eval
on steroids, configurable and extensible, but by default trapping
(Perl) STDOUT, STDERR, warnings, exceptions, would-be exit codes, and
return values from boxed blocks of test code.

The values collected by the latest trap can then be queried or tested
through a special trap object.

%description -l pl.UTF-8
Moduł przeznaczony głównie (ale nie wyłącznie) do użycia w skryptach
testowych: blokowy eval na sterydach, konfigurowalny i rozszerzalny,
ale domyślnie przechwytujący (perlowe) STDOUT, STDERR, ostrzeżenia,
wyjątki, potencjalne kody wyjścia i wartości zwracane z ograniczonych
bloków kodu testowego.

Zgromadzone wartości z ostatniej pułapki mogą być następnie odpytywane
lub testowane poprzez specjalny obiekt pułapki.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Trap.pm
%{perl_vendorlib}/Test/Trap
%{_mandir}/man3/Test::Trap*.3pm*
