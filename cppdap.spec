Summary:	C++11 implementation of the Debug Adapter Protocol
Summary(pl.UTF-8):	Implementacja Debug Adapter Protocol w C++11
Name:		cppdap
%define	tag_ver	1.58.0-a
Version:	%(echo %{tag_ver} | tr -d -)
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/google/cppdap/tags
Source0:	https://github.com/google/cppdap/archive/dap-%{tag_ver}.tar.gz
# Source0-md5:	24465ac50c76a19565f07f4a723b78cb
Patch0:		%{name}-shared.patch
URL:		https://github.com/google/cppdap
BuildRequires:	cmake >= 3.13
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	nlohmann-json-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cppdap is a C++11 library ("SDK") implementation of the Debug Adapter
Protocol (<https://microsoft.github.io/debug-adapter-protocol/>),
providing an API for implementing a DAP client or server.

%description -l pl.UTF-8
cppdap to implementacja w postaci biblioteki ("SDK") C++11 protokołu
Debug Adapter Protocol
(<https://microsoft.github.io/debug-adapter-protocol/>), dostarczająca
API do implementowania klienta lub serwera DAP.

%package devel
Summary:	Header files for cppdap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cppdap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for cppdap library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cppdap.

%prep
%setup -q -n %{name}-dap-%{tag_ver}
%patch0 -p1

%build
%cmake -B build \
	-DCPPDAP_USE_EXTERNAL_NLOHMANN_JSON_PACKAGE=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libcppdap.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/dap
%{_libdir}/cmake/cppdap
