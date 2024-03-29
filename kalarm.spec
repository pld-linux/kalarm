Summary:	KAlarm - A personal alarm scheduler
Summary(de.UTF-8):	KAlarm - Ein persönliches Terminplanungsprogramm
Summary(pl.UTF-8):	KAlarm - Osobisty program do przypominania
Name:		kalarm
Version:	2.1.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.astrojar.org.uk/linux/download/%{name}-%{version}.kde3.tar.bz2
# Source0-md5:	a04fecd18da5b5532f915c1307c66fa5
Patch0:		kde-ac260-lt.patch
URL:		http://www.kde-apps.org/content/show.php?content=9966
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdepim-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Provides:	kdepim-kalarm
Obsoletes:	kdepim-kalarm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlarm is a personal alarm message, command and email scheduler. It
lets you set up personal alarm messages which pop up on the screen at
the chosen time, or you can schedule commands to be executed or emails
to be sent. Also includes an alarm daemon.

%description -l de.UTF-8
KAlarm ist ein persönliches Terminplanungsprogramm das via Meldung
oder E-Mail bescheid gibt. Es ermöglicht eigene Alarm-Nachrichten
einzustellen die später bei der gewünschten Zeit auf dem Bildschirm
erscheinen, oder Tätigkeiten die gemacht werden sollen sowohl wie
E-Mails die verschickt werden sollen einzuplanen. Das Packet enthält
auch ein Hintergrundprogramm.

%description -l pl.UTF-8
KAlarm to osobisty program do planowania i przypominania poprzez
uruchomienie polecenia lub pocztą elektroniczną. Umożliwia ustawienie
własnej wiadomości alarmowej, która wyskoczy na ekranie o wybranym
czasie albo zaszeregowanie poleceń do wykonania lub poczty do
wysłania. Zawiera także demona obsługującego przypominanie.

%prep
%setup -q
%patch0 -p1

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
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{ven,ve}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS Changelog README README.libical
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libkalarm*.so.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_desktopdir}/kalarm.desktop
%{_datadir}/apps/kalarm*
%{_datadir}/apps/kconf_update/kalarm*.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kalarm*.pl
%{_datadir}/apps/libkholidays
%{_datadir}/services/kresources/kalarm
%{_datadir}/services/kresources/*.desktop
%{_datadir}/autostart/*.desktop
%{_iconsdir}/crystalsvg/*x*/*/%{name}.png
