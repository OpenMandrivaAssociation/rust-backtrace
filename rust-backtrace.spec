# Generated by rust2rpm 11
%bcond_without check
%global debug_package %{nil}

%global crate backtrace

Name:           rust-%{crate}
Version:        0.3.60
Release:        2
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
