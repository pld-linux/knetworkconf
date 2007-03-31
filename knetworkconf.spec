Summary:	KDE network configuration tool
Summary(pl.UTF-8):	Narzędzie do konfiguracji sieci dla KDE
Name:		knetworkconf
Version:	0.6.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/knetworkconf/%{name}-%{version}.tar.bz2
# Source0-md5:	b2b68c8e16122eb442643aa246daa988
URL:		http://knetworkconf.sourceforge.net/
Patch0:		%{name}-ac.patch
Patch1:		%{name}-am.patch
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

%description -l pl.UTF-8
KNetworkConf to aplikacja KDE do konfigurowania ustawień TCP/IP na
maszynie linuksowej. Możliwości:
- konfigurowanie urządzeń sieciowych
- włączanie/wyłączanie urządzeń sieciowych
- ustawianie domyślnej bramki i urządzenia sieciowego dla niej
- ustawianie serwerów DNS, nazw domeny i maszyny
- edycja pliku /etc/hosts (znanych hostów).

Obsługuje także PLD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
sed -i 's/doc //' Makefile.am
for i in knetworkconf/*.ui.h;do mv $i `basename $i .ui.h`.h;done;

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
