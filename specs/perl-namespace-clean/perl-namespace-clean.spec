# $Id$
# Authority: dag
# Upstream: Florian Ragwitz <rafl@debian.org>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name namespace-clean

Summary: Keep imports and functions out of your namespace
Name: perl-namespace-clean
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/namespace-clean/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/namespace-clean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(B::Hooks::EndOfScope) >= 0.07
BuildRequires: perl(ExtUtils::MakeMaker)%{?!el5: >= 6.31}
BuildRequires: perl(FindBin)
BuildRequires: perl(Package::Stash) >= 0.03
BuildRequires: perl(Sub::Identify) >= 0.04
BuildRequires: perl(Sub::Name) >= 0.04
BuildRequires: perl(Symbol)
BuildRequires: perl(Test::More)%{?!el5: >= 0.88}
BuildRequires: perl(vars)
Requires: perl(B::Hooks::EndOfScope) >= 0.07
Requires: perl(Package::Stash) >= 0.03
Requires: perl(Sub::Identify) >= 0.04
Requires: perl(Sub::Name) >= 0.04
Requires: perl(Symbol)

### remove autoreq Perl dependencies
%filter_from_requires /^perl*/d
%filter_setup


%description
When you define a function, or import one, into a Perl package, it will
naturally also be available as a method. This does not per se cause problems,
but it can complicate subclassing and, for example, plugin classes that are
included via multiple inheritance by loading them as base classes.

The namespace::clean pragma will remove all previously declared or imported
symbols at the end of the current package's compile cycle. Functions called in
the package itself will still be bound by their name, but they won't show up as
methods on your class or instances.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{?!el5:%{__make} test}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/namespace::clean.3pm*
%dir %{perl_vendorlib}/namespace/
#%{perl_vendorlib}/namespace/clean/
%{perl_vendorlib}/namespace/clean.pm

%changelog
* Thu Dec 16 2010 Steve Huff <shuff@vecna.org> - 0.18-1
- Updated to version 0.18.

* Mon Jun  7 2010 Christoph Maser <cmaser@gmx.de> - 0.17-1
- Updated to version 0.17.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.13-1
- Updated to version 0.13.

* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.11-2
- Fix dependencies

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Update to version 0.11.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
