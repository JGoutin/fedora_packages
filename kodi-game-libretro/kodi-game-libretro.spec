%global kodi_addon game.libretro
%global kodi_addon_license GPL-2.0-or-later
%global kodi_version 20
%global kodi_codename Nexus

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Epoch:          1
Version:        20.1.0
Release:        1%{?dist}
Summary:        Compatibility add-on for Kodi allowing Libretro cores as game add-ons
License:        %{kodi_addon_license}
URL:            https://github.com/kodi-game/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz
BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(tinyxml)
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64}


%description
This Kodi add-on provides a wrapper that allows Libretro cores to be loaded as
Kodi game add-ons. Libretro cores are shared libraries that use the Libretro
API, so the wrapper is responsible for translating function calls between the
Libretro API and the Game API.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
%cmake3
%cmake3_build
cat > %{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="addon">
  <id>%{name}</id>
  <extends>kodi.desktop</extends>
  <name>Kodi - Libretro Compatibility</name>
  <summary>%{summary}</summary>
  <url type="homepage">%{url}</url>
  <url type="help">https://kodi.wiki/view/Games</url>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>%{kodi_addon_license}</project_license>
</component>
EOF


%install
%cmake3_install
install -Dpm 0644 %{name}.metainfo.xml %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/
%{_metainfodir}/%{name}.metainfo.xml


%changelog
%autochangelog
