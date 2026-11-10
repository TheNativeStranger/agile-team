---
name: architecture-work
description: "Mimari işin akışı: netleştirme, neyi-nasıl-ne ile kararı, HLD, LLD, çizim, danışma kurulu incelemesi. Çözüm Mimarı her mimari konuda kullanır."
---
# Mimari iş akışı

Bütün çıktılar çalışılan klasörde `docs/architecture/` altında durur:

| Çıktı | Yer | Şablon |
|---|---|---|
| Karar matrisi | `decisions/<konu>.md` | `${CLAUDE_PLUGIN_ROOT}/skills/architecture-work/templates/decision-matrix.md` |
| ADR | `adr/NNN-<karar>.md` | `.../templates/adr.md` |
| HLD | `hld/<konu>-hld.md` | `.../templates/hld.md` |
| Grooming kaydı | `grooming/<konu>.md` | Görüş, risk, soru, çaba, karar |
| LLD | `lld/<konu>/parts/<rol>.md`, birleşen `lld/<konu>-lld.md` | `.../templates/lld.md` |
| Çizimler | `diagrams/<konu>.drawio` | `agile-team:drawio` |

## Akış
1. **Netleştir:** İş hedefi, kapsam, kısıtlar, işlevsel olmayan gereksinimler, entegrasyonlar, veri ve KVKK. Bilinmeyenleri açık soru olarak yaz. Gerekirse uzmana danış.
2. **Neyi, nasıl, ne ile:** Karar matrisini doldur, seçenekleri karşılaştır, önerini yaz.
3. **Onay:** Yönü kullanıcıya göster. Onay yoksa HLD yazılmaz.
4. **HLD ve üst düzey çizimler:** Bağlam, bileşen, entegrasyon, dağıtım görünümleri. Gerekirse TOGAF'tan ilgili aşamayı ve ArchiMate görünümünü kullan.
5. **Grooming:** Beş yardımcının hepsi aynı anda HLD'yi okur; görüş, risk, soru ve çaba söyler. Çözüm Mimarı `grooming/<konu>.md` dosyasına birleştirir, çelişkileri karara bağlar. Kullanıcının kararı gereken nokta varsa sorar.
6. **LLD bölümleri:** Herkes kendi bölümünü `lld/<konu>/parts/<rol>.md` dosyasına yazar.

   | Bölüm | Sahibi |
   |---|---|
   | Kapsam ve HLD bağlantısı, API sözleşmeleri, Veri modeli, Akışlar, Güvenlik ayrıntıları, Açık sorular | `solution-designer` |
   | Servis ve modül yapısı, Yapılandırma, Uygulama adımları | `java-expert` |
   | Kafka topic ve olay şemaları, Hata ve yeniden deneme | `kafka-expert` |
   | OpenShift kaynakları, Gözlemlenebilirlik | `openshift-expert` |
   | Test yaklaşımı | `test-expert` |

7. **Birleştirme:** `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/merge-lld.py" docs/architecture/lld/<konu>`. Solution Designer tutarsızlıkları işaretler.
8. **Çapraz inceleme:** Her uzman birleşen belgeyi kendi açısından okur. Düzeltmeyi bölümün sahibi yapar, sonra yeniden birleştirilir.
9. **Betik kontrolü:** Token harcamayan kontroller:
   - `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check-docs.py" <belge> --type hld|lld|adr`
   - `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check-drawio.py" <çizim>`

## Bitti tanımı
- Neyi, nasıl, ne ile soruları karar matrisinde cevaplı
- Zorunlu bölümler dolu, betik kontrolleri geçti
- Grooming kaydı yazıldı, her uzman kendi bölümünü yazdı ve çapraz inceledi
- Her önemli karar için ADR var
- Belgedeki çizim bağlantıları gerçek dosyalara gidiyor
- Açık sorular ve riskler sahipleriyle yazılı
