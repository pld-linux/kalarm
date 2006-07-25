Summary:	KAlarm - A personal alarm scheduler
Summary(de):	KAlarm - Ein persönliches Terminplanungsprogramm
Summary(pl):	KAlarm - Osobisty program do przypominania
Name:		kalarm
Version:	1.4.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.astrojar.org.uk/linux/download/%{name}-%{version}.kde3.tar.bz2
# Source0-md5:	5afe685ac914cad08e98c140e836f364
URL:		http://www.kde-apps.org/content/show.php?content=9966
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	qt-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-core >= 3.0
Requires:	qt >= 3.1
Provides:	kdepim-kalarm
Obsoletes:	kdepim-kalarm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlarm is a personal alarm message, command and email scheduler. It
lets you set up personal alarm messages which pop up on the screen at
the chosen time, or you can schedule commands to be executed or emails
to be sent. Also includes an alarm daemon.

%description -l de
KAlarm ist ein persönliches Terminplanungsprogramm das via Meldung
oder E-Mail bescheid gibt. Es ermöglicht eigene Alarm-Nachrichten
einzustellen die später bei der gewünschten Zeit auf dem Bildschirm
erscheinen, oder Tätigkeiten die gemacht werden sollen sowohl wie
E-Mails die verschickt werden sollen einzuplanen. Das Packet enthält
auch ein Hintergrundprogramm.

%description -l pl
KAlarm to osobisty program do planowania i przypominania poprzez
uruchomienie polecenia lub poczt± elektroniczn±. Umo¿liwia ustawienie
w³asnej wiadomo¶ci alarmowej, która wyskoczy na ekranie o wybranym
czasie albo zaszeregowanie poleceñ do wykonania lub poczty do
wys³ania. Zawiera tak¿e demona obs³uguj±cego przypominanie.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

rm -r $RPM_BUILD_ROOT%{_datadir}/applnk/Applications
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS Changelog README README.libical
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kalarm.desktop
%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_datadir}/apps/kalarm*
%{_iconsdir}/crystalsvg/16x16/apps/%{name}.png
%{_iconsdir}/crystalsvg/32x32/apps/%{name}.png
%{_iconsdir}/crystalsvg/48x48/apps/%{name}.png
%{_datadir}/autostart/*.desktop
