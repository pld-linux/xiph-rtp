Summary:	Reference implementation for rtp-vorbis and rtp-theora
Summary(pl):	Wzorcowa implementacja rtp-vorbis i rtp-theora
Name:		xiph-rtp
Version:	0.1
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://downloads.xiph.org/releases/xiph-rtp/%{name}-%{version}.tar.gz
# Source0-md5:	2b4d7e8b2103bed383d46cd069582e31
URL:		http://www.xiph.org/
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reference implementation for rtp-vorbis and rtp-theora.

%description -l pl
Wzorcowa implementacja rtp-vorbis i rtp-theora.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install vorbisrtp theorartp vorbisrtp-client theorartp-client $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
