%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Itinerary display application
Name:		itinerary
Version:	20.12.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Positioning)
BuildRequires:	cmake(Qt5Location)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KPimPkPass)
BuildRequires:	cmake(KPimItinerary)
BuildRequires:	cmake(KPublicTransport)
BuildRequires:	cmake(KOSMIndoorMap)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(ZLIB)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	cmake
BuildRequires:	ninja

%description
Itinerary display application

%files -f kde-itinerary.lang
%{_bindir}/itinerary
%{_libdir}/libSolidExtras.so
%{_libdir}/qt5/qml/org/kde/solidextras/libsolidextrasqmlplugin.so
%{_libdir}/qt5/qml/org/kde/solidextras/qmldir
%{_datadir}/applications/org.kde.itinerary.desktop
%{_datadir}/icons/hicolor/*/*/itinerary.*
%{_datadir}/knotifications5/itinerary.notifyrc
%{_datadir}/metainfo/org.kde.itinerary.appdata.xml
%{_datadir}/qlogging-categories5/org_kde_itinerary.categories

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kde-itinerary
