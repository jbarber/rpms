# Authority: atrpms
# Upstream: Chip Turner <cturner@redhat.com>

%define rname RPM-Specfile

Summary: Perl module for creating rpm packages of other perl modules.
Name: perl-RPM-Specfile
Version: 1.12
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPM-Specfile/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHIPT/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
Requires: perl
BuildRequires: perl

%description
Simple module for creation of RPM Spec files.  Used by cpanflute2 to turn CPAN
tarballs into RPM modules.
See the included script cpanflute2 for usage; documentation coming soon.

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%{__rm} -rf %{buildroot}%{perl_sitearch} \
		%{buildroot}%{perl_archlib}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/

%changelog
* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.12-1
- Fixed site -> vendor. (Matthew Mastracci)

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.12-0
- Updated to release 1.12.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 1.11-0
- Initial package. (using DAR)
