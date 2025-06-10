pkgname=sleex-settings
pkgver=0.1.0
pkgrel=1
pkgdesc="A tool to manage sleex settings easily"
arch=('x86_64')
license=('GPL3')
depends=('gtk4' 'python' 'sleex')


build() {
  cd "${srcdir}"
  meson --prefix=/usr build --reconfigure
  ninja -C build
}

package() {
  cd "${srcdir}/build"
  DESTDIR="${pkgdir}" ninja install
}