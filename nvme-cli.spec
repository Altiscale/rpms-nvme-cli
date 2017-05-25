Name:           nvme-cli
Version:        1.3
Release:        1%{?dist}
Summary:        NVMe management command line interface

License:        GPLv2+
URL:            https://github.com/linux-nvme/nvme-cli
Source0:        https://github.com/linux-nvme/%{name}/archive/v%{version}.tar.gz


BuildRequires: binutils 
BuildRequires: coreutils 
BuildRequires: cpio 
BuildRequires: diffutils 
BuildRequires: elfutils 
BuildRequires: file 
BuildRequires: findutils 
BuildRequires: gcc 
BuildRequires: gdb 
BuildRequires: glibc-devel 
BuildRequires: glibc-headers 
BuildRequires: grep 
BuildRequires: gzip 
BuildRequires: kernel-headers 
BuildRequires: make 
BuildRequires: ncurses-base 
BuildRequires: sed 
BuildRequires: tar 



%description
nvme-cli provides NVM-Express user space tooling for Linux.

%prep
%setup


%build
make PREFIX=/usr 


%install
make install-bin install-man PREFIX=%{buildroot}%{_usr}


%files
%{_sbindir}/nvme
%{_mandir}/man1/nvme*.gz


%changelog
* Wed May 24 2017 ryan.tokarek@sap.com - 1.3-1
- Update to v1.3
- Adapted from Cent OS 7 spec file for Cent OS 6
- v1.3 removes udev dependency

* Tue May 31 2016 luto@kernel.org - 0.7-1
- Update to 0.7

* Fri Mar 18 2016 luto@kernel.org - 0.5-1
- Update to 0.5

* Sun Mar 06 2016 luto@kernel.org - 0.4-1
- Update to 0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3.20160112gitbdbb4da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 luto@kernel.org - 0.2-2.20160112gitbdbb4da
- Update to new upstream commit, fixing #49.  "nvme list" now works.

* Wed Jan 13 2016 luto@kernel.org - 0.2-1.20160112gitde3e0f1
- Initial import.

