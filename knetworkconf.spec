
%define		_rc	beta1

Summary:	KDE network configuration tool
Summary(pl):	Narzêdzie do konfiguracji sieci dla KDE
Name:		knetworkconf
Version:	0.5
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}%{_rc}.tar.bz2
# Source0-md5:	56f37d2c72fdab200a5249f2d482e394
URL:		http://knetworkconf.sourceforge.net/
BuildRequires:	kdelibs-devel >= 8:3.1
BuildRequires:	sed >= 4.0
Requires:	kdebase-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNetworkConf is a KDE application to configure TCP/IP settings on a
Linux machine. 
Features:
- Configure network devices.
- Enable/disable network devices.
- Configure default gateway and gateway device.
- Configure DNS servers, domain name and machine name.
- Edit /etc/hosts file (known hosts).

Supports also PLD.

%description -l pl
KNetworkConf to aplikacja KDE do konfigurowania ustawieñ TCP/IP na
maszynie linuksowej. Mo¿liwo¶ci:
- konfigurowanie urz±dzeñ sieciowych
- w³±czanie/wy³±czanie urz±dzeñ sieciowych
- ustawianie domy¶lnej bramki i urz±dzenia sieciowego dla niej
- ustawianie serwerów DNS, nazw domeny i maszyny
- edycja pliku /etc/hosts (znanych hostów).

Obs³uguje tak¿e PLD.

%prep
%setup -q -n %{name}-%{version}%{_rc}

%build
sed -i 's/doc //' Makefile.am

%{__make} -f admin/Makefile.common cvs

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

# RedHatoooze ?!
mv $RPM_BUILD_ROOT%{_libdir}/kde3/Configuration/KDE/Network/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

sed -i 's/locolor\/32x32\/apps\///' \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

echo "Categories=Qt;KDE;SystemSetup;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

mv $RPM_BUILD_ROOT{%{_iconsdir},%{_pixmapsdir}}/network_card.png

mv $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/knetworkconf
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}/pixmaps
%dir %{_datadir}/apps/%{name}/backends
%attr(755,root,root) %{_datadir}/apps/%{name}/backends/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_pixmapsdir}/network_card.png
