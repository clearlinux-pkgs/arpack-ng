#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : arpack-ng
Version  : 3.8.0
Release  : 15
URL      : https://github.com/opencollab/arpack-ng/archive/3.8.0/arpack-ng-3.8.0.tar.gz
Source0  : https://github.com/opencollab/arpack-ng/archive/3.8.0/arpack-ng-3.8.0.tar.gz
Summary  : Collection of Fortran77 subroutines designed to solve large scale eigenvalue problems
Group    : Development/Tools
License  : BSD-3-Clause
Requires: arpack-ng-lib = %{version}-%{release}
Requires: arpack-ng-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : cmake
BuildRequires : eigen-data
BuildRequires : git
BuildRequires : openblas
BuildRequires : openmpi-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(eigen3)
BuildRequires : python3
BuildRequires : python3-dev

%description
1. Purpose
-------
This directory contains example drivers that call ARPACK subroutines
__aupd.f and __eupd.f to solve various eigenvalue problems using regular,
shift-invert or other special modes (such as Cayley, Bucking etc.)
These drivers illustrate how to set various ARPACK parameters to solve
different problems in different modes.  They provide a guideline on how
to use ARPACK's reverse communication interface.  The user may modify
any one of these drivers, and supply his/her own matrix vector
multiplication routine to solve the problem of his/her own interest.
These drivers are installed in the following subdirectories.

%package dev
Summary: dev components for the arpack-ng package.
Group: Development
Requires: arpack-ng-lib = %{version}-%{release}
Provides: arpack-ng-devel = %{version}-%{release}
Requires: arpack-ng = %{version}-%{release}

%description dev
dev components for the arpack-ng package.


%package lib
Summary: lib components for the arpack-ng package.
Group: Libraries
Requires: arpack-ng-license = %{version}-%{release}

%description lib
lib components for the arpack-ng package.


%package license
Summary: license components for the arpack-ng package.
Group: Default

%description license
license components for the arpack-ng package.


%prep
%setup -q -n arpack-ng-3.8.0
cd %{_builddir}/arpack-ng-3.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656089748
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build-avx2;
make test || :
cd ../clr-build-avx512;
make test || :

%install
export SOURCE_DATE_EPOCH=1656089748
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/arpack-ng
cp %{_builddir}/arpack-ng-3.8.0/COPYING %{buildroot}/usr/share/package-licenses/arpack-ng/a8322a2036b23080e6706a894c314b9f477dce58
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/arpack/arpackdef.h
/usr/include/arpack/arpackicb.h
/usr/include/arpack/debug.h
/usr/include/arpack/stat.h
/usr/lib64/cmake/arpack-ng/arpack-ng-config-version.cmake
/usr/lib64/cmake/arpack-ng/arpack-ng-config.cmake
/usr/lib64/libarpack.so
/usr/lib64/pkgconfig/arpack.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libarpack.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libarpack.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libarpack.so.2.1.0
/usr/lib64/glibc-hwcaps/x86-64-v4/libarpack.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libarpack.so.2
/usr/lib64/glibc-hwcaps/x86-64-v4/libarpack.so.2.1.0
/usr/lib64/libarpack.so.2
/usr/lib64/libarpack.so.2.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/arpack-ng/a8322a2036b23080e6706a894c314b9f477dce58
