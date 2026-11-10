---
name: architecture-work
description: "Mimari işin akışı: netleştirme, neyi-nasıl-ne ile kararı, HLD, LLD, çizim, danışma kurulu incelemesi. Baş Mimar her mimari konuda kullanır."
---
# Mimari iş akışı

Bütün çıktılar çalışılan klasörde `docs/architecture/` altında durur:

| Çıktı | Yer | Şablon |
|---|---|---|
| Karar matrisi | `decisions/<konu>.md` | `${CLAUDE_PLUGIN_ROOT}/skills/architecture-work/templates/decision-matrix.md` |
| ADR | `adr/NNN-<karar>.md` | `.../templates/adr.md` |
| HLD | `hld/<konu>-hld.md` | `.../templates/hld.md` |
| LLD | `lld/<konu>-lld.md` | `.../templates/lld.md` |
| Çizimler | `diagrams/<konu>.drawio` | `agile-team:drawio` |

## Akış
1. **Netleştir:** İş hedefi, kapsam, kısıtlar, işlevsel olmayan gereksinimler, entegrasyonlar, veri ve KVKK. Bilinmeyenleri açık soru olarak yaz.
2. **Uzman görüşü al:** Yalnızca konuya katkı verecek uzmanları aynı anda çağır.
3. **Neyi, nasıl, ne ile:** Karar matrisini doldur, seçenekleri karşılaştır, önerini yaz.
4. **Onay:** Yönü kullanıcıya göster. Onay yoksa HLD yazılmaz.
5. **HLD ve üst düzey çizimler:** Bağlam, bileşen, entegrasyon, dağıtım görünümleri. Gerekirse TOGAF'tan ilgili aşamayı ve ArchiMate görünümünü kullan.
6. **LLD ve ayrıntılı çizimler:** `solution-designer` yazar: sıra, sınıf, veri modeli, olay akışı.
7. **Kurul incelemesi:** İlgili uzmanlar belgeyi bölüm bölüm okur. Bulguları Baş Mimar birleştirir; çelişkiler iki taraflı yazılır.
8. **Betik kontrolü:** Token harcamayan kontroller:
   - `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check-docs.py" <belge> --type hld|lld|adr`
   - `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check-drawio.py" <çizim>`

## Bitti tanımı
- Neyi, nasıl, ne ile soruları karar matrisinde cevaplı
- Zorunlu bölümler dolu, betik kontrolleri geçti
- İlgili uzmanların incelemesi yazıldı
- Her önemli karar için ADR var
- Belgedeki çizim bağlantıları gerçek dosyalara gidiyor
- Açık sorular ve riskler sahipleriyle yazılı
