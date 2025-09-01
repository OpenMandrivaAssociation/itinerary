%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Itinerary display application
Name:		itinerary
Version:	25.08.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/itinerary-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6Location)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KF6NetworkManagerQt)
BuildRequires:	cmake(KF6UnitConversion)
BuildRequires:	cmake(KPim6PkPass)
BuildRequires:	cmake(KPim6Itinerary)
BuildRequires:	cmake(KPublicTransport)
BuildRequires:	cmake(KOSMIndoorMap)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(ZLIB)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libical)
#BuildRequires:	cmake(KHealthCertificate)
BuildRequires:	qml(org.kde.kitemmodels)
BuildRequires:	qml(org.kde.kopeninghours)
Requires:	qml(org.kde.kitemmodels)
Requires:	qml(org.kde.kopeninghours)

%rename plasma6-itinerary

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Itinerary display application.

%files -f %{name}.lang
%{_bindir}/itinerary
%{_libdir}/libSolidExtras.so
%{_qtdir}/plugins/kf6/kfilemetadata/kfilemetadata_itineraryextractor.so
%{_qtdir}/plugins/kf6/thumbcreator/itinerarythumbnail.so
%{_qtdir}/qml/org/kde/solidextras/libsolidextrasqmlplugin.so
%{_qtdir}/qml/org/kde/solidextras/qmldir
%{_datadir}/applications/org.kde.itinerary.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.itinerary.svg
%{_datadir}/knotifications6/itinerary.notifyrc
%{_datadir}/metainfo/org.kde.itinerary.appdata.xml
%{_datadir}/qlogging-categories6/org_kde_itinerary.categories
