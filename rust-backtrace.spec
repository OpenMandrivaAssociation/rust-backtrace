# Generated by rust2rpm 11
%bcond_without check
%global debug_package %{nil}

%global crate backtrace

Name:           rust-%{crate}
Version:        0.3.40
Release:        2%{?dist}
Summary:        Library to acquire a stack trace (backtrace) at runtime in a Rust program

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/backtrace
Source:         %{crates_source}
# Initial patched metadata
# * No windows/osx
# * Exclude CI files, https://github.com/alexcrichton/backtrace-rs/pull/131
Patch0:         backtrace-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to acquire a stack trace (backtrace) at runtime in a Rust program.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+addr2line-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+addr2line-devel %{_description}

This package contains library source intended for building other packages
which use "addr2line" feature of "%{crate}" crate.

%files       -n %{name}+addr2line-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+backtrace-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-sys-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace-sys" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+cpp_demangle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cpp_demangle-devel %{_description}

This package contains library source intended for building other packages
which use "cpp_demangle" feature of "%{crate}" crate.

%files       -n %{name}+cpp_demangle-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+dladdr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dladdr-devel %{_description}

This package contains library source intended for building other packages
which use "dladdr" feature of "%{crate}" crate.

%files       -n %{name}+dladdr-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+findshlibs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+findshlibs-devel %{_description}

This package contains library source intended for building other packages
which use "findshlibs" feature of "%{crate}" crate.

%files       -n %{name}+findshlibs-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+gimli-symbolize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gimli-symbolize-devel %{_description}

This package contains library source intended for building other packages
which use "gimli-symbolize" feature of "%{crate}" crate.

%files       -n %{name}+gimli-symbolize-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+libbacktrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libbacktrace-devel %{_description}

This package contains library source intended for building other packages
which use "libbacktrace" feature of "%{crate}" crate.

%files       -n %{name}+libbacktrace-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+libunwind-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libunwind-devel %{_description}

This package contains library source intended for building other packages
which use "libunwind" feature of "%{crate}" crate.

%files       -n %{name}+libunwind-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+memmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memmap-devel %{_description}

This package contains library source intended for building other packages
which use "memmap" feature of "%{crate}" crate.

%files       -n %{name}+memmap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+rustc-serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-serialize-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-serialize" feature of "%{crate}" crate.

%files       -n %{name}+rustc-serialize-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serialize-rustc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialize-rustc-devel %{_description}

This package contains library source intended for building other packages
which use "serialize-rustc" feature of "%{crate}" crate.

%files       -n %{name}+serialize-rustc-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serialize-serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialize-serde-devel %{_description}

This package contains library source intended for building other packages
which use "serialize-serde" feature of "%{crate}" crate.

%files       -n %{name}+serialize-serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+unix-backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unix-backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "unix-backtrace" feature of "%{crate}" crate.

%files       -n %{name}+unix-backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# https://github.com/rust-lang/backtrace-rs/issues/204
%ifarch %{ix86} ppc64le aarch64
  %cargo_test || :
%else
  %cargo_test
%endif
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 0.3.40-1
- Update to 0.3.40

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 09:21:35 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.30-2
- Regenerate

* Tue Jun 04 2019 Josh Stone <jistone@redhat.com> - 0.3.30-1
- Update to 0.3.30

* Mon Jun 03 2019 Josh Stone <jistone@redhat.com> - 0.3.28-1
- Update to 0.3.28

* Sat Jun 01 2019 Josh Stone <jistone@redhat.com> - 0.3.26-1
- Update to 0.3.26

* Wed May 15 08:23:12 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.16-1
- Update to 0.3.16

* Fri Apr 05 2019 Josh Stone <jistone@redhat.com> - 0.3.15-1
- Update to 0.3.15

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.14-2
- Do not pull optional dependencies

* Tue Feb 19 2019 Josh Stone <jistone@redhat.com> - 0.3.14-1
- Update to 0.3.14

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Josh Stone <jistone@redhat.com> - 0.3.13-1
- Update to 0.3.13

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.12-2
- Run tests in infrastructure

* Wed Dec 12 2018 Josh Stone <jistone@redhat.com> - 0.3.12-1
- Update to 0.3.12

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Josh Stone <jistone@redhat.com> - 0.3.9-1
- Update to 0.3.9

* Wed May 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8

* Fri May 04 2018 Josh Stone <jistone@redhat.com> - 0.3.7-1
- Update to 0.3.7

* Sat Apr 14 2018 Josh Stone <jistone@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-2
- Rebuild for rust-packaging v5

* Thu Jan 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-1
- Initial package
