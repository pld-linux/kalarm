#
# TODO:
# - kttsd support (bcond --without kttsd)
#   ^^^^^ (B)Rs
#
Summary:	KAlarm
Summary(de):	KAlarm
Summary(pl):	KAlarm
Name:		kalarm
Version:	1.4.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.astrojar.org.uk/linux/download/%{name}-%{version}.kde3.tar.bz2
# Source0-md5:	5600afd5bb5bef102eb448c21f02c417
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
KAlarm lets you configure personal messages to be displayed, commands
to be executed, or emails to be sent, at scheduled times. It allows
you to choose the message font and color, how often to repeat, whether
to display an advance reminder, whether to speak the message or play a
sound when it is displayed, and whether to cancel the alarm if it
can't be triggered on time (e.g. if you are logged out at the time).
As well as using the graphical interface to configure alarms, you can
use the command line, and there is a DCOP interface for other
applications.

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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL README README.libical
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kalarm.desktop
%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_datadir}/applnk/Applications/kalarm.desktop
%{_datadir}/apps/kalarm*
%{_iconsdir}/crystalsvg/16x16/apps/%{name}.png
%{_iconsdir}/crystalsvg/32x32/apps/%{name}.png
%{_iconsdir}/crystalsvg/48x48/apps/%{name}.png
%{_datadir}/autostart/*.desktop
