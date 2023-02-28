Summary:	Apple Lossless Audio Decoder
Summary(pl.UTF-8):	Dekoder Apple Lossless Audio
Name:		alac_decoder
Version:	0.2.0
Release:	1
License:	MIT
Group:		Applications/Sound
# original URL is dead
#Source0:	http://craz.net/programs/itunes/files/%{name}-%{version}.tgz
# ...so use gentoo distfiles
Source0:	http://distfiles.gentoo.org/distfiles/%{name}-%{version}.tgz
# Source0-md5:	cec75c35f010d36e7bed91935b57f2d1
# NXDOMAIN
#URL:		http://craz.net/programs/itunes/alac.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apple Lossless Audio Decoder.

%description -l pl.UTF-8
Dekoder Apple Lossless Audio.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -W -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install alac $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/alac
