#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		grantlee-editor
Summary:	Grantlee Editor
Name:		ka5-%{kaname}
Version:	22.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3bde36027902b48ef830265c270848f4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-kimap-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities and tools to manage themes in KDE PIM applications.

%description -l pl.UTF-8
Narzędzia do zarządzania motywami w aplikacjach KDE PIM.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/contactprintthemeeditor
%attr(755,root,root) %{_bindir}/contactthemeeditor
%attr(755,root,root) %{_bindir}/headerthemeeditor
%ghost %{_libdir}/libgrantleethemeeditor.so.5
%attr(755,root,root) %{_libdir}/libgrantleethemeeditor.so.*.*.*
%{_desktopdir}/org.kde.contactprintthemeeditor.desktop
%{_desktopdir}/org.kde.contactthemeeditor.desktop
%{_desktopdir}/org.kde.headerthemeeditor.desktop
%{_datadir}/config.kcfg/grantleethemeeditor.kcfg
%{_datadir}/qlogging-categories5/grantleeditor.categories
%{_datadir}/qlogging-categories5/grantleeditor.renamecategories
