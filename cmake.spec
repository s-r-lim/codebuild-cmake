Name: cmake
Version: 3.31.2
Release: ${CODEBUILD_BUILD_NUMBER}%{?dist}
Summary: CMake Binary Package
ExclusiveArch: x86_64 aarch64
License: BSD
Provides: cmake
Requires: openssl-devel
Source0: cmake-%{version}.tar.gz


%description
Binary CMake

%prep
%setup -q

%install
%define license_dir %{_datadir}/licenses/cmake/
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp ./bin/* $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{license_dir}
cp ./doc/cmake-3.31/Copyright.txt $RPM_BUILD_ROOT%{license_dir}Copyright.txt
cp ./doc/cmake-3.31/cmcurl/COPYING $RPM_BUILD_ROOT%{license_dir}COPYING_cmcurl
cp ./doc/cmake-3.31/cmlibarchive/COPYING $RPM_BUILD_ROOT%{license_dir}COPYING_cmlibarchive
cp ./doc/cmake-3.31/cmliblzma/COPYING $RPM_BUILD_ROOT%{license_dir}COPYING_cmliblzma
cp ./doc/cmake-3.31/cmlibrhash/COPYING $RPM_BUILD_ROOT%{license_dir}COPYING_cmlibrhash
cp ./doc/cmake-3.31/cmnghttp2/COPYING $RPM_BUILD_ROOT%{license_dir}COPYING_cmnghttp2
cp ./doc/cmake-3.31/cmzlib/Copyright.txt $RPM_BUILD_ROOT%{license_dir}Copyright.txt_cmzlib
cp ./doc/cmake-3.31/cmsys/Copyright.txt $RPM_BUILD_ROOT%{license_dir}Copyright.txt_cmsys
cp ./doc/cmake-3.31/cmzstd/LICENSE $RPM_BUILD_ROOT%{license_dir}LICENSE_cmzstd

cp -r ./share/aclocal $RPM_BUILD_ROOT/%{_datadir}/.
cp -r ./share/bash-completion $RPM_BUILD_ROOT/%{_datadir}/.
cp -r ./share/vim $RPM_BUILD_ROOT/%{_datadir}/.
cp -r ./share/cmake-3.31 $RPM_BUILD_ROOT/%{_datadir}/cmake

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{license_dir}/Copyright.txt
%{license_dir}/COPYING_cmcurl
%{license_dir}/COPYING_cmlibarchive
%{license_dir}/COPYING_cmliblzma
%{license_dir}/COPYING_cmlibrhash
%{license_dir}/COPYING_cmnghttp2
%{license_dir}/Copyright.txt_cmsys
%{license_dir}/Copyright.txt_cmzlib
%{license_dir}/LICENSE_cmzstd
%{_datadir}/aclocal
%{_datadir}/bash-completion/*
%{_datadir}/cmake/*
%{_datadir}/vim


