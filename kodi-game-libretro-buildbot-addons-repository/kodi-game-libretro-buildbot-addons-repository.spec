%global kodi_addon repository.kodi_libretro_buildbot_game_addons
%global kodi_addon_license GPL-3.0-or-later

Name:           kodi-game-libretro-buildbot-addons-repository
Epoch:          1
Version:        1.0.1
Release:        1%{?dist}
Summary:        Kodi repository of game add-ons based on the libretro buildbot binaries
License:        %{kodi_addon_license}
URL:            https://github.com/zach-morris/kodi_libretro_buildbot_game_addons
Source0:        %{url}/raw/main/%{kodi_addon}.zip
Source1:        %{url}/raw/main/LICENSE.txt
BuildRequires:  libappstream-glib
Requires:       kodi-game-libretro
Supplements:    kodi-game-libretro
BuildArch:      noarch


%description
This Kodi repository provides libretro cores game add-ons.
Theses add-ons are build directly using binaries from the Libretro buildbot
(https://buildbot.libretro.com) and are updated on a weekly basis.


%prep
%autosetup -c


%build
cp %{SOURCE1} .
cat > %{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="addon">
  <id>%{name}</id>
  <extends>kodi.desktop</extends>
  <name>Kodi - Libretro buildbot game add-ons repository</name>
  <summary>%{summary}</summary>
  <url type="homepage">%{url}</url>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>%{kodi_addon_license}</project_license>
</component>
EOF


%install
install -Dpm 0644 %{kodi_addon}/* -t %{buildroot}%{_datadir}/kodi/addons/%{kodi_addon}
install -Dpm 0644 %{name}.metainfo.xml %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE.txt
%{_datadir}/kodi/addons/%{kodi_addon}/
%{_metainfodir}/%{name}.metainfo.xml


%changelog
%autochangelog
