# TODO: optflags
Summary:	Apple Lossless Audio Decoder
Summary(pl.UTF-8):   Dekoder Apple Lossless Audio
Name:		alac_decoder
Version:	0.1.1
Release:	0.1
License:	BSD-like
Group:		Applications/Sound
Source0:	http://craz.net/programs/itunes/files/%{name}-%{version}.tar.gz
# Source0-md5:	06f358b8aa185dcb3d1e2d80f89570c3
URL:		http://craz.net/programs/itunes/alac.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apple Lossless Audio Decoder.

%description -l pl.UTF-8
Dekoder Apple Lossless Audio.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install alac $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/alac
